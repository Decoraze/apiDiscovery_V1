from subprocess import run 
import subprocess

def command_group_run(url):
    
    #------------------SubDirectory------------------#

    #command to run subdirectory finder to find all the subdirectories of the url that was given
    commandSubFinder = ["subfinder","-d",(str(url)),"-nW","-t","100","-o",(str(url)+"Subfinder.txt")]
    #output = run(command, capture_output=True).stdout
    #variable that stores the output of the subprocess and runs the command for subdirectory
    subfinder = subprocess.Popen(commandSubFinder, stdout=subprocess.PIPE ).communicate()[0]


    #---------------------HTTPX---------------------#
    #command to find the other rare ports that might be in use that is not the cmmon ports like 443, 8080 etc. 
    commandHttpx = ["httpx","-list",(str(url)+"Subfinder.txt"), "-probe", "-sc", "-ip","-cl","-ct","-pa", "-nc","-o",(str(url)+"Httpx.txt"),"|","grep","200"]#add grepping for 200s and SUCCESS 
    #command to run the command given above by using subprocess library
    httpx = subprocess.Popen(commandHttpx, stdout=subprocess.PIPE).communicate()[0]

    #command to filter the output: cat *url*Httpx.txt | grep 200
    commandStrip = ["cat", (str(url)+"Httpx.txt")]
    strip = subprocess.Popen(commandStrip, stdout=subprocess.PIPE)
    commandGrep = ['grep','200']
    output = subprocess.check_output((commandGrep), stdin=strip.stdout).decode("utf-8")
    print(type(output))
    
    #filtering even more by putting the output into a list and filtering from there using a nested loop
    outputlst = output.split("\n")
    links = []
    for requests in outputlst:
        link = (requests.split(' '))[0]

        if link not in links and link != '':
            links.append(link)
    #print(links) #use this for testing 

    #---------------------FeroxBuster--------------------#
    numRecursions = int(input("Please input the number of times you want to do the recursion: "))
    wordList = str(input("Please input the wordlist(include the path) you would want to use for the recursion: "))
    for urls in links:
        print(urls)
        commandFerox = ["feroxbuster","-u",urls,"-w","/usr/share/seclists/Discovery/Web-Content/directory-list-1.0.txt","-t","100","-f","-o",(str(urls[8::])+"Feroxbuster.txt"),"--force-recursion","--time-limit","20m","--silent","-d",str(numRecursions),"-e"]
        feroxBuster = subprocess.Popen(commandFerox,stdout=subprocess.PIPE).communicate()[0]

        #----------------------Nuclei---------------------#
        #Filtering#
        
        nucleiTemplates = str(input("Please input the template you want to use for the testing.E.g. /nuclei-templates/...: " ))
        commandNuclei = ["nuclei","-l",""]



def main():
    link = input("Please input the url you want to use. E.g. twiiter.com/facebook.com/thedogapi.com: ")
    command_group_run(link)


if __name__ == "__main__":
    main()
