##
#
# Gabriel Ghiuzan (914067@swansea.ac.uk) & Slade Brooks (963336@swansea.ac.uk) (2018)
#
##

#string word;
#while()
#{
#    word = checkValue(file line)
#    if(word.equals("cs-150"))
#    {
#        while()
#        {
#            word = checkValue(file line)
#        }
#    }
#}



def classifier(input):
    input_tokens = input.split()
    print(input_tokens)

    for word in input_tokens:
        if word == "what":
            intent = "what"
        elif word == "how":
            intent = "how"
        else:
            intent = "none"

def main():
    input = "what is a multiplexer?"
    classifier(input)

main()
