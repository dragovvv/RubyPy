#Made By IT-Err0r And Dragovvv

class Ruby():

    #The Print Function
    def ruby_print(text,type):

        if type == "str":
            script = open("script.rb","a")
            script.write(f'print "{text}" \n')
            script.close()

        elif type == "int" or type == "float" or type == "var":
            script = open("script.rb","a")
            script.write(f'print {text} \n')
            script.close()

        else:
            print("Worng Data Type")
        
    #The Puts Function
    def ruby_print_Line(text,type):
        
        if type == "str":
            script = open("script.rb","a")
            script.write(f'puts "{text}" \n')
            script.close()

        elif type == "int" or type == "float" or type == "var":
            script = open("script.rb","a")
            script.write(f'puts {text} \n')
            script.close()

        else:
            print("Worng Data Type")

    #The int Variable Function
    def ruby_create_var(varname,value,type):
        
        if type == "int" or type == "float":

            script = open("script.rb","a")
            script.write(f'{varname} = {value} \n')
            script.close()

        elif type == "str":

            script = open("script.rb","a")
            script.write(f'{varname} = "{value}" \n')
            script.close()

    #The Comments Function
    def ruby_comment(cmnt):
        
        script = open("script.rb","a")
        script.write(f'#{cmnt}\n')
        script.close()
