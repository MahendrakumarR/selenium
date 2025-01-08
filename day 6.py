"""
DAY6
----
Robot class
contextClick
doubleClick

"""
"""
How will you perform rightClick?

    Use the contextClick() method from the Actions class.

How will you perform doubleClick?

    Use the doubleClick() method from the Actions class.

Write a code for Robot class?

    Robot robot = new Robot();

In which package is the Robot class available?

    The Robot class is available in the java.awt package.

What exception does the Robot class throw?

    The Robot class throws the AWTException.

What is the method to perform rightClick?

    The method is contextClick() in the Actions class.

What is the method to perform doubleClick?

    The method is doubleClick() in the Actions class.

Write a code to copy a text using the Robot class?

    Robot robot = new Robot();
    robot.keyPress(KeyEvent.VK_CONTROL);
    robot.keyPress(KeyEvent.VK_C);
    robot.keyRelease(KeyEvent.VK_C);
    robot.keyRelease(KeyEvent.VK_CONTROL);

Write a code to paste a text using the Robot class?

    Robot robot = new Robot();
    robot.keyPress(KeyEvent.VK_CONTROL);
    robot.keyPress(KeyEvent.VK_V);
    robot.keyRelease(KeyEvent.VK_V);
    robot.keyRelease(KeyEvent.VK_CONTROL);

In which class is contextClick() available?

    The contextClick() method is available in the Actions class.

In which class is doubleClick() available?

    The doubleClick() method is available in the Actions class.

"""
"""
QUESTION 1
----------
URL : https://www.facebook.com/

NOTE: Type email in email textbox and cut  the email using Robot class 
      Paste that email in password text  using Robot class 

"""


