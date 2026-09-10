init offset = -1

################################################################################
## Circle (소속/직책) 지원 시스템 및 파서 확장
################################################################################

python early hide:
    import renpy.parser

    # 1. 3연속 문자열 ("who" "circle" "what") 지원 확장 say_statement
    if hasattr(renpy.parser, 'statements') and hasattr(renpy.parser.statements, 'default'):
        _orig_say_statement = renpy.parser.statements.default

        def _enhanced_say_statement(l, loc):
            state = l.checkpoint()

            # 3연속 문자열 검사 ("who" "circle" "what")
            s1 = l.string()
            if s1 is not None:
                s2 = l.string()
                if s2 is not None:
                    s3 = l.triple_string() or l.string()
                    if s3 is not None:
                        # 3연속 문자열 감지: s1=who, s2=circle, s3=what
                        who_expr = '_say_circle(%r, %r)' % (s1, s2)
                        rv = renpy.parser.finish_say(l, loc, who_expr, s3)
                        if rv is not None:
                            l.expect_eol()
                            l.expect_noblock('say statement')
                            l.advance()
                            return rv

            # 3연속 문자열이 아니면 렉서 위치 복원 후 원래 say_statement 실행
            l.revert(state)
            return _orig_say_statement(l, loc)

        # statements.default 및 say_statement 교체
        renpy.parser.statements.default = _enhanced_say_statement
        renpy.parser.say_statement = _enhanced_say_statement


init python:
    # 2. 런타임에서 who, circle을 받아 캐릭터를 생성/반환하는 헬퍼 함수
    def _create_say_circle(who, circle=None):
        if circle is not None:
            return Character(who, show_circle=circle)
        return Character(who)

    _say_circle = _create_say_circle

    # 3. Character 생성자 확장 (circle 매개변수 지원)
    _orig_Character = Character

    def Character(name=renpy.character.NotSet, *args, **kwargs):
        if "circle" in kwargs:
            circle_val = kwargs.pop("circle")
            if circle_val is not None:
                kwargs["show_circle"] = circle_val
        return _orig_Character(name, *args, **kwargs)
