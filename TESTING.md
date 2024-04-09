# Testing

When looking to approach testing for this project, I considered when is best to use automated testing and manual testing. To my understanding, I know that automated testing is useful for scenarios when the test cases are time-consuming for humans, or the tests are repeated several times over time. Manual testing is more suitable for cases when test cases only need to be run once or twice. So in this instance with this project, manual testing is best suited due to the fact the tests I will perform through development and implementation, will be simple, small tests run once or twice.

## Testing during Development

* Throughout the process of making this website, I tested my code using the preview window extension within VS Code and in the chrome browser. With chrome browser I could use Chrome Developer Tools troubleshoot any spacing issues in the CSS or Javascript bugs within the console log.
* I would also consistently commit and push work to Github to then view live site and check responsiveness on my mobile and tablet devices, as well as passing onto friends and family to test on their devices.
* I have also tested my site in the main browsers available, which include:

  * Google Chrome
  * Mozilla Firefox
  * Apple Safari
  * Microsoft Edge

### Testing the Home page

I made sure whilst in development phase and implementation phase I was regularly testing all the interactive elements on my page. On my home page, this included:

* Pop-up 'Close' button
  * **Expected:** Intro pop-up to close and the timer to start from 15
  * **Tested:** Click on the 'Close' button
  * **Result:** Pop-up closed but the timer did not start from 15, it had started on page load
  * ****Action:**** Examined the code and re-wrote the timer function code, using true and false states to manage when the timer would start and pause (explained in more detail below [Timer Issues](#timer-issues))

* Pop-up 'Play Again' button
  * **Expected:** Button to refresh the page
  * **Tested:** Let the timer run out and the pop-up to appear, then click on the 'Play Again' button
  * **Result:** Pop-up not closing or refreshing the page
  * **Action:** Moving the function to within the openPopUpTime function (explained in more detail below [Buttons in pop-ups](#buttons-in-pop-ups-not-working))

* Interactive ingredients
  * **Expected:** The ingredient name should appear as an overlay on the ingredient disc when hovered over and cause an action when clicked - either trigger the coffee cup image to change if it is correct, or if it is an incorrect guess it should trigger a try again message
  * **Tested:** Rolled mouse over all ingredient discs and then each tested and for each drink name instance for correct triggers
  * **Result:** All overlays working effectively and triggering the relevant functions within javascript
  * **Action:** None

* 'How to play' button
  * **Expected:** Bring up the Coffee Menu game instructions pop-up and pause the timer, the when 'Close' button clicked the pop-up should close and the timer restart
  * **Tested:** Click on the button during game play
  * **Result:** The pop-up appears but the timer continued to run
  * **Action:** I had to look into rewriting my code for the timer to include pause functionality using true and false states to stop and start the timer with the button clicks (explained in more detail below [Timer Issues](#timer-issues))

* 'Reset game' button
  * **Expected:** The page will reload
  * **Tested:** Clicked on the 'Reset Game' button during game play
  * **Result:** The page reloaded
  * **Action:** None

* 'Submit' button for email form
  * **Expected:** To only submit if all fields have been filled in correctly
  * **Tested:** Left each field blank or invalid and then clicking the 'Submit' button
  * **Result:** Form preventing from submitting and the user prompted through messages to not leave fields blank and to include '@' in the email field
  * **Action:** None

I wanted to check my 404 page worked correctly:

* Incorrect URL test
  * **Expected:** The 404 page to be called to redirect the user to the correct URL for the home page
  * **Tested:** Put random characters in the URL
  * **Result:** The 404 page was called successfully and the link back to the home page on that page worked effectively
  * **Action:** None

I then regularly tested responsiveness:

* Desktop responsiveness
  * **Expected:** All text and visuals to be clearly visible, no overhanging off the page
  * **Tested:** Tested on my laptop screen as well as larger external monitor
  * **Result:** Everything fluidly increased/decreased in size for the screen responsively. All readable and useable
  * **Action:** None

* Tablet responsiveness
  * **Expected:** All text and visuals to be clearly visible, no overhanging off the page, overlays to appear when clicked
  * **Tested:** Interacted with the site on my tablet as well as in chrome developer tools in tablet sizes
  * **Result:** All visible and clear, overlays on ingredients appearing when clicked. The footer overhanging the initial instructions pop-up
  * **Action:** The footer CSS to be updated to reduce the size of the text inside using a media query, as well as removing an unnecessary line of text in the instructions pop up that said 'How to Play' and this reduced the pop-up's height.

* Mobile responsiveness
  * **Expected:** All text and visuals to be clearly visible, no overhanging off the page, overlays to appear when clicked
  * **Tested:** Interacted with the site on my tablet as well as in chrome developer tools in tablet sizes
  * **Result:** All visible and clear, overlays on ingredients appearing when clicked. The footer overhanging the initial instructions pop-up. Some of the text too big for all the content to fit on the screen.
  * **Action:** The footer CSS to be updated to reduce the size of the text inside, as well as removing an unnecessary line of text in the instructions pop up that said 'How to Play' and this reduced the pop-up's height. Edited some font sizes in media queries to make text fit better in the window.

Here are the bugs I encountered and fixed as I went through the development and implementation of my site:

* **Random drink generator section**
  * Initially I had used "location.reload()" to reset the drink name section at the top of the page, which refreshed the page, meaning my score and order counters were not going up in score as they kept resetting with the page refresh.
  * To fix, I created a separate function to get the randomized drink from the array, that is called through the variable "drinkName". Then, when it is called through the "playerWin()" function, it calls another drink without refreshing the page.

* **Random drink sometimes showing same drink twice in game play**
  * I put in a while loop that would check the new randomized drink against the previous correctly guessed drinks array (these were each added as an to a separate array once completed) to make sure it did not display the same drink twice. If it was the same, it re-ran the randomiser until it wasn't the same.

  ![While loop for random drink generator](assets/readme-images/while-loop.png)

* **Order count and Score count**
  * Initially I tried out different code to get the order count and score count to increase with each correct answer but it did not work initially.
  * After troubleshooting I rewrote my code so that each increase in points was written in a separate function and then called within the playerWin function, which allowed it to start the function when the playerWin function is triggered, whereas before it was not being triggered by anything.

* #### **Timer issues**
  * I had a lot of issues getting the timer to function the way I wanted it to:
    * It would not refresh to full 15 seconds when a pop-up was closed
    * It would run twice as fast if the user clicked on the 'how to play' button during game play and returned to the game*
    * The timer would start before the user clicks off the first pop-up

    ![Old timer code](assets/readme-images/old-timer-function-code.png)

  * I decided I needed to look at a completely different way of creating a timer function so did some research on google, looking for pause functions. I found an example where someone had used true and false statements to change the state of the timer function with an if statement to stop and start the timer with the click of certain button (Please see link to this reference in the [Code](#code) section below).
  * With this concept in mind, I recreated my code (see below) and changed the state between true and false within the pop-up button and the how to play button. So the state when the page loads is 'true' so the timer won't start until the 'close' button is pressed and the state is changed to 'false'.
  * This meant that the setInterval function that was in my old code, did not have chance to start twice and inturn double the speed of the count down of the timer.
  * After this, I then changed the value of the 'time' variable to 16 wherever I wanted the timer to start counting down again (I found when I used the value 15, it was showing as 14 straight away as it counted down from 15 immediately, so I decided on using 16 to rectify this.)

  ![New timer code](assets/readme-images/new-timer-function-code.png)
  
  * I also found that I needed to move the 'time' value change into its own setTimeOut function after the pop-up state change, as it was originally in the same setTimeOut function and was starting to count down well before the pop-up had disappeared.

  ![Refresh timer code](assets/readme-images/refresh-timer-code.png)

* #### **Buttons in pop-ups not working**
  * The button to "Play Again" at the end of a game were not working see code snippet below:
  ![Pop-up button issue code](assets/readme-images/pop-up-button-code-issue.png)
  * Resolved by moving the function to within the openPopUpTime function, as I realised this would call the function in the right order after the "innerhtml" had been changed rather than before, which was why it was not working properly.
  ![Pop-up button resolved code](assets/readme-images/pop-up-button-code-fix.png)

### Testing the Contact Form page
* **Email JS not feeding in parameters**
  * Initially when putting together my email template and testing it with EmailJS, the message, email address and name were not pulling through into the email sent to my inbox.
  * Upon further inspection, I realised I needed to add parameters for each input into the JS file, which I had not been able to follow clearly in the Code Institute tutorial, but found the solution while looking at the emailJS tutorials on their site to resolve. 
![Send mail code](assets/readme-images/send-mail-code.png)

![Send mail success](assets/readme-images/emailjs-success.png)

### Testing the Thank you page
* Successfully re-directs back to site after 5 seconds when tested.

## Validator Testing

### W3C Validator
I ran my site pages through the W3C validator and I received one error for a missing alt tag for an image on my index page. 

![Alt tag required screenshot](assets/readme-images/w3c-validator-check.png)

I corrected the code and all three pages now return no html errors.

### CSS Jigsaw Validator
I put the CSS stylesheet through the Jigsaw Validator and found one Parse error.

![CSS error screenshot](assets/readme-images/css-validator-check.png)

I corrected this error, as the syntax was incorrect for CSS.

## Lighthouse Performance Testing

Using the Chrome Developer Tools Lighthouse reports, I was able to test the performance of my site pages and improve it as a result.

### Desktop
My initial desktop performance came out as below:

  ![Initial site performance](assets/readme-images/desktop-lighthouse.png)

To improve my score, I did the following:
* Updated the coffee menu pop-up image to a higher res version.
* Added alt tags to all my images.

My score in accessibility, best practices and SEO improved after all these changes. However due to improving the quality of the coffee menu image as it had suggested, the performance reduced slightly, but all now in the green:

  ![Final site performance](assets/readme-images/desktop-lighthouse-after.png)

### Mobile

The performance came out as:

![Mobile site performance after](assets/readme-images/mobile-lighthouse.png)

* Performance on mobile could still be improved by reducing image sizes, but this is difficult to do when the images need to be large enough for larger screens in this particular instance.

## JS Hint Testing
I ran all three of my Javascript files through this JS Hint validator. 

![JS Hint game JS file performance after](assets/readme-images/jshint-warnings.png)
The validator came back highlighting some unnecessary semicolons as well as a couple of variables not being used, which I took out and cleaned up so it now returns no warnings.

![JS Hint email JS file performance after](assets/readme-images/email-js-hint.png)
The validator came back clean apart from mentioning an unused variable and an undefined variable for the send-email.js code, but this is because they are declared/used within the html code.

The modal-pop-up.js came back with no errors or warnings.