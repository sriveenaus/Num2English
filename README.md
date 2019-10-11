INSTRUCTIONS:
=============
1)docker build -t num2eng .
2)docker images | grep num2eng
3)docker run -ti 6597d81b1382


FEATURES SUPPORTED IN THIS docker SERVICE:
==========================================
1)Converts  a number to English word
2) Only takes positive integers
3)THe most important of all is that since it takes a keyboard input
you have to run the docker image in "-ti" ==>Interactive mode to be able 
to provide a keyboard input integer . Otherwise the docker service num2Eng will through a 
EOF line error 
4) It works upto 100s of trillions!!!!

Sample output for clarification:
=================================
1)docker build -t num2eng .
2)docker images | grep num2eng
num2eng  latest              6597d81b1382        14 seconds ago      917MB

3)docker run -ti 6597d81b1382
Enter a Number: 1234
1234
one thousand two hundred thirty four   
Enter a Number: 09732-94r7
Traceback (most recent call last):
  File "./num2eng.py", line 44, in <module>
    main()
  File "./num2eng.py", line 40, in main
    num = int (input("Enter a Number: "))
ValueError: invalid literal for int() with base 10: '09732-94r7'
