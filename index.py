class Ruby():

    #The Print Function(*Made By Dragovvv*)
    def ruby_print_txt(text):

        script = open("script.rb","a")
        script.write(f'print "{text}" ')
        script.close()
        
    #The Puts Function(*Made By IT-Err0r*)
    def ruby_print_Line_txt(text):
        
        script = open("script.rb","a")
        script.write(f'puts "{text}" ')
        script.close()

    #The Print Function(*Made By IT-Err0R*)
    def ruby_print_num(number):

        script = open("script.rb","a")
        script.write(f'print {number} ')
        script.close()
        
    #The Puts Function(*Made By IT-Err0r*)
    def ruby_print_Line_num(number):
        
        script = open("script.rb","a")
        script.write(f'puts {number} ')
        script.close()


    #The Variable Function(*Made By IT-Err0r*)
    def ruby_var_int(varname,value: int):
        
        script = open("script.rb","a")
        script.write(f'{varname} = {value} ')
        script.close()
        
    #The Print Var Function(*Made By IT-Err0r*)
    def ruby_var_str(varname,value: str):
        
        script = open("script.rb","a")
        script.write(f'{varname} = "{value}" ')
        script.close()
