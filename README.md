## Yososerial Auto generate payloads 

#### There is nothing distinctive; the tool's function is to expedite the process of creating payloads for exploiting insecure deserialization

### requirements :
* Download the ysoserial tool [Download](https://github.com/frohoff/ysoserial)
* Install Java 11
```
sudo apt-get install openjdk-11-jdk
```


### Using :
```

─# python3 Gengadexploit.py

┏┳┳┓ ┏┓    ┓     ┓╹                                                                                                                                                                            
 ┃┃┃ ┃┃┏┓┓┏┃┏┓┏┓┏┫ ┓                                                                                                                                                                           
┗┛┻┛━┣┛┗┻┗┫┗┗┛┗┻┗┻ ┗                                                                                                                                                                           
          ┛                                                                                                                                                                                    
ENG. Khaled Alshammri                                                                                                                                                                          
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               
Enter the command: whoami
Enter the path of gadgets.txt file: gadgets.txt

```

### Pic
![Cool GIF](https://raw.githubusercontent.com/ik0z/yososerial-auto/main/ezgif-3-eac3fb925e.gif)

### Create your own gadgets
```
─# java -jar ysoserial-all.jar
```
Copy the output inside text file then 
```
─# cat output.txt | tr -d ' ' | cut -d '@' -f 1 > gadgets.txt
```

