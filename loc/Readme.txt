# Counting Lines of Code

Original: <http://codekata.com/kata/kata13-counting-code-lines/>

Write a utility that counts the number of lines of actual code in a Java source file.

A line is counted if it contains something other than whitespace or text in a comment.

Examples:

```java
// This file contains 3 lines of code
public interface Dave {
   /**
    * count the number of lines in a file
    */
    int countLines(File inFile); // not the real signature!
}
```

```java
/*****
* This is a test program with 5 lines of code
*  \/* no nesting allowed!
//*****//***/// Slightly pathological comment ending...

public class Hello {
    public static final void main(String [] args) { // gotta love Java
        // Say hello
      System./*wait*/out./*for*/println/*it*/("Hello/*");
    }
}
```

