# -*- coding: utf-8 -*-

def print_s(string):i
#{
    print(string, end = "")#;
#}

def main():
#{
    for y in range(-1, 10):
#    #{
        for x in range(-1, 10):
#        #{
            if y < 0:
#            #{
                if x < 0:
#                #{
                    ch = "  "
#                #}
                elif x == 0:
#                #{
                    ch = "|"
#                #}
                else:
#                #{
                    ch = "%3d" %x
#                #}
#            #}
            elif y == 0:
#            #{
                if x < 0:
#                #{
                    ch = "--"
                #}
                elif x == 0:
                #{
                    ch = "+"
                #}
                else:
                #{
                    ch = "---"
                #}
            #}
            else:
            #{
                if x < 0:
                #{
                    ch = "%2d" %y
                #}
                elif x == 0:
                #{
                    ch = "|"
                #}
                else:
                #{
                    ch = "%3d" %(y * x)
                #}
            #}

            print_s(ch)
        #}

        print()
#}

if __name__ == "__main__":
#{
    main()
#}

