# Instacook

For my Milestone 3 project I have created a personalised Cookbook web application, where the user can log into their account, search for recipes, add their own recipes, as well as edit their own recipes and delete when required. They can also give star ratings to their recipes to help them highlight and bookmark their favourites and make them easier to find in the future.

![Screen mock-ups of Instacook website](assets/readme-images/mock-up-picture-coffee-cram.png)


[Link to Instacook live site](https://kateuj.github.io/coffee_cram/)

## Table of Contents

1. [Planning & Development](#planning--development)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Languages](#languages)
6. [Media Queries](#media-queries)
7. [Software](#software)
8. [Code](#code)
9. [Credits](#credits)

# Planning & Development #

### Site Purpose
This game is been designed mainly to create a positive emotional response through entertainment. It could also be used as an informal and fun introduction for barista training where the trainer could use this as a tool to test their trainee's knowledge of drinks before and after training to have a constructive comparison on how their knowledge has been built and any areas for improvement.

### Target Audience

Broadly, the game is aimed at anyone with an interest in coffee, which could include people seeking entertainment in the form of a quiz, but also as mentioned above for trainee barista to revise their knowledge, as well as barista trainers to used as an energy boosting / ice-breaking tool in training sessions with their trainees.

### User Needs

#### User Stories
1. User interested in coffee wants seeks coffee content based entertainment.
![Home page screenshot](assets/readme-images/home-page-screenshot.png)
The user gets a quick overview of the ingredients required for drinks before they can go quickly into their game play for entertainment. They can also refer back to the coffee menu if required, with the 'How To Play' button.

2. A barista trainee wanting to test their drink making knowledge.
![Home page screenshot](assets/readme-images/home-page-screenshot.png)
The user can refresh their memories of ingredient combinations or choose to just go straight into the game by closing the instructions window to test their knowledge from what they know already.
They can also refer back to the coffee menu if required, with the 'How To Play' button.
![End of game pop-up screenshot](assets/readme-images/pop-up-with-finished-game.png)
The game will show the user at the end of the game what drinks they got right, so they know what to focus on in future revision time.
![Get in touch screenshot](assets/readme-images/contact-page.png)
They may also follow the call to action to get more information on barista training and submit a Get in touch form on the contact page.
![Thank you re-direct page screenshot](assets/readme-images/thank-you-page.png)
Once submitted, they are directed to a thank you page to confirm their message has been submitted and then redirected straight back to the game page in 5 seconds without them having to click anything, to make their user experience as straight forward as possible.

3. A barista trainer uses the game as a tool to test their trainees' knowledge.
![Home page mobile screenshot](assets/readme-images/mobile-home-page.png)
A barista trainer would get users to open the page on their phones collectively to access the game as a quick and fun ice breaker before commencing a practical course. The mobile view makes it easy for the site to be accessed anywhere.

### Site Objectives

* Test user's knowledge of coffee drink making.
* Give the user a positive emotion experience with bright and fun colours and imagery.
* Build responsive game that works on mobile, tablet and desktop.
* Make the game easy to use with rules explained.
* Easy to navigate around and find key information.
* The option to view instructions anytime, to help the user revise the ingredients for each drink and refresh their memory easily.
* A good UI site flow.
* Provide the users with a way of contacting me and submitting a message to my email inbox.
* To be accessible for screen readers.
* To be able to reset the game easily.
* Links to the creator's social media in footer.

* Nice to have feature would be a shopping list

### Approach

* User experience design will be planned and carefully considered when designing the flow of layout of the game.
* The site will provide users links through to my social media accounts to contact me.
* The content of the site will be family-friendly and accessible to all.
* The game design will be consistent and visually engaging for the users.

![Information Flow of the site](assets/readme-images/information-flow.png)

### Research

I looked at other javascript-based games before making a decision on what I wanted to create, to see what was possible using the javascript concepts and skills I have learnt recently.

Sites included:
* [Burger Make](https://www.culinaryschools.org/kids-games/burger-maker/)
* [Hang Man](https://codepen.io/cathydutton/pen/JjpxMm)

Thoughts noted:
* Minimalist design.
* Responsive design.
* Game on one page.
* Pop up with instructions included.

All of the above, I have reflecting in the design of my own website.

### Wireframes

I used Figma and Balsamiq to plan and design my wireframes and user journey. I like using Figma in particular because it always you to brainstorm and keep all ideas and inspiration in one place as a singular visual to refer back to, which has been very useful throughout the project. I designed my site in mobile format initially before moving onto bigger screens, to ensure responsiveness was considered, especially since most users will predominantly use their phones to access this game.
I have changed a features along the way after considering user experience, for instance, I chose not to add a drop down menu at the top of the mobile version due to the site only being two pages long and felt it unnecessary in the end, due to the link to the contact page being below the game. If I had included an accordion nav bar at the top it would have pushed the game content further down the screen, meaning the user may need to scroll to see all the ingredients, which I decided was not acceptable for a good user experience.

#### Mobile Design Wireframe

![mobile design wireframe](assets/readme-images/mobile-wireframes.png)

#### Tablet Design Wireframe

![tablet design wireframe](assets/readme-images/tablet-wireframes.png)

#### Desktop Design Wireframe

![desktop design wireframe](assets/readme-images/desktop-wireframes.png)

[Link to my Figma page](https://www.figma.com/file/sE1FXwAGFZf3FEYIDAB8l0/Milestone-2---Coffee-Cram?type=design&node-id=0%3A1&mode=design&t=spVJTdSswAGCzuT1-1)

### Colour Scheme

After looking at coffee based content, branding and cafe simulator games, I found a lot of them to have quite muted, bland colour palettes, due to coffee being brown and having to work with that colour predominantly. However I was adamant to make this game as visually exciting as possible, so I looked at retro game palettes as well as bright 'vaporwave' colours to form my own striking colour palette to engage the user. The retro look and feel was intentional to invoke a cosy, reminiscent experience for users.
I made sure I had a good mix of high contrasting colours for good readability, which I have learn is important to consider when designing a website or application to ensure inclusivity for all users.

![Colour Scheme](assets/readme-images/colour-palette.png)

### Graphics

I was conscious that with 6 different ingredients and over 6 different variations of drinks, that this game could end up looking visually confusing if not approached carefully. I chose to create simple, isometric, flat graphics, which are in-keeping with the retro feel, but also creating a minimalist look and feel to keep the game approachable and not too overwhelming for the user.

![Coffee Cup Graphic](assets/readme-images/cappuccino.png)

### Typography

I chose a retro pixelated style font for headings and the logo for the game to accentuate the retro feel of the game, but also coupled it with Rubik, a simple, easy to read sans-serif font, for any body text sentences etc. to maintain good readability and in turn a good user experience.

![Typefaces used](assets/readme-images/fonts.png)

### Javascript coding approach

I made a point of keeping my game code separate from the email JS code and the modal pop-up code, to improve usability of the code for future coding users. With this in mind, I have commented on each function to provide explanation of each to make my code and thought process as clear as possible to future viewers. I have also used a mixture of plain Javascript and Jquery to demonstrate my knowledge.

# Features #

## Existing Features

### General

* My site is fully responsive and can be viewed and used effectively on all screen sizes down to 320px width by 480px height.
* I have considered readability contrast carefully for all visual elements.
* I have included a Favicon page tab icon to make the page look professional and consistent.

![Favicon screenshot](assets/readme-images/favicon-screenshot.png)

### Logo
![Logo in navigation bar](assets/readme-images/logo.png)

* I created my simple text logo using the Silkscreen font to give it the retro gaming feel.

## Game page

![Home page screenshot](assets/readme-images/home-page-screenshot.png)

* To keep things clear I have sectioned out the page, so that the ingredients are on the left and the coffee drink is on the right to be created and filled up by the user. In mobile and tablet, the cup appears at the top with the ingredients at the bottom so the user instinctively reads the drink name first, sees the cup to fill and then proceeds to the ingredients to make choices.

### Instructions pop-up

![Game instructions pop-up screenshot](assets/readme-images/game-pop-up-screenshot.png)

* I created an animated gif for the centre of the landing page to add to the initial visual impact of the site to draw users in. I have kept it in a hand-drawn style to keep it fun and intriguing for a younger audience and to get my own personality across to the user to make it feel more casual and relatable.

### Random drink generator

![Drink title generator screenshot](assets/readme-images/random-drink-generator.png)

* This title prints a random drink from an array in the script-game.js file.
* I have used a while loop to make sure no drink appears twice during one game. The loop checks the users correct drink answers array against the original drink name array. This user array has also been useful to then print out the drinks the user got correct in a pop up at the end of game play, to help them know where to focus on next time to improve their score.

![Javascript code for drink name generator screenshot](assets/readme-images/drink-name-random-code.png)

### Ingredient text overlays

![Ingredient with hover overlays screenshot](assets/readme-images/ingredient-drawer-image-overlays.png)

* When the user clicks on an ingredient in the mobile version, or hovers over in the desktop version, the name of ingredient appears as a text overlay over the graphic. I felt this was intuitive for the user and also maintained the minimalist visual due to there not being an overload of text on the page.

### Changing coffee cup graphic

![Coffee cup graphic screenshot](assets/readme-images/coffee-cup-change.png)

* The coffee cup image changes if the correct ingredient is clicked for the drink name that has been generated at the top of the page. It go through each step, gradually filling up with each ingredient until the drink is complete.

### Timer, score count and order count

![Timer, score count and order count screenshot](assets/readme-images/timer-and-counts.png)

* Each drink gets a 15 second timer for the user to guess the ingredient sequence correctly. For every incorrect ingredient clicked, the player loses 5 points in their score, and for every correctly guessed drink sequence, they get 10 points. The order count also keeps track of how many drinks have been successfully completed so far.

### Try again pop-up

![Try again pop-up screenshot](assets/readme-images/try-again-pop-up.png)

* For each incorrect ingredient clicked, a timed pop-up appears prompting the user to try again and check the how to play section if unsure.

### Well done pop-up

![Well done pop-up screenshot](assets/readme-images/well-done-pop-up.png)

* A well done pop-up appears for every correct sequence completed so the user knows the game has progressed and they are moving onto the next drink.

### End of game pop-up / Out of time pop-up

![End of game pop-up screenshot](assets/readme-images/pop-up-with-score.png)

* Conscious I wanted to make this as intuitive as possible for giving the user feedback as this is can be used as a training tool, I have created logic that tailors the pop-up message based on if they answer any questions correctly, if time ran out, or if they completed the game.
* The user array I created to use in the while loop for the random drink generator (to make sure no drink appears twice during one game) allows me to print out the drinks the user got correct in a pop up at the end of game play, to help them know where to focus on next time to improve their score.

![End of game pop-up no drinks correct screenshot](assets/readme-images/pop-up-with-no-score.png)

![End of game pop-up all drinks correct screenshot](assets/readme-images/pop-up-with-finished-game.png)

### Footer

![Footer screenshot](assets/readme-images/footer.png)

* I have included links to my Instagram profile in the footer along with an icon that links to the contact form page. This way if the user is more driven by icons than text, they will instinctively know to click the email icon to get in touch, versus the users who might be encouraged or prompted to contact from the text and 'click here' link I have included within the footer too.
* The external link to Instagram opens a separate window, whereas the internal link to my contact form redirects to the contact page within the same window, which is good practice when designing a user journey and saves several windows opening for the user for the same website.

## Get in touch page

![Get in touch screenshot](assets/readme-images/contact-page.png)

* I have included a functional contact form created using emailjs for users to contact me.

### Contact Form

![Contact Form screenshot](assets/readme-images/contact-form.png)

* All inputs are required
* The contact form checks the input is valid before sending and if not it will alert the user - the email input will not work unless a proper email address is added, and you cannot leave any field blank.

![Contact Form pop up screenshot](assets/readme-images/invalid-input-error-email-form.png)

## Thank you page

![Thank you re-direct page screenshot](assets/readme-images/thank-you-page.png)

* A quick message to the user to confirm their message has been submitted and to redirect them back to the game page within 5 seconds.

## Error 404 page

![Error 404 page screenshot](assets/readme-images/error-404-page.png)

* Should any errors occur, the user will be directed to this page. I have included this page in the sendmail js file function, should the form not successfully submit. The page has a button that links back to the game page, so the user can return back to the main site easily and quickly.

## Possible Future Features

* Background music for ambience
* Confetti animation when the user guesses the correct sequence
* More drink variations

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


# Deployment

## GitHub pages
I used GitHub pages to deploy my site. This required me to go to my project repository and then:
1. Click on the 'Settings' tab.
2. Select 'Pages' from the menu that appears on the left.
3. Select 'Deploy from a branch'.
4. Select 'Main' in the drop-down menu called 'Select Branch'.
5. Then alongside 'Main', there is a folder dropdown where you select '/Root'.
6. Click 'Save' button.
7. Refresh the page and a link to the live project will appear at the top of the page.

## Forking a GitHub repository
Forking allows users to make a copy of an original repository in GitHub and view and make changes to it without changing the original repository.
To create a fork:
1. Once logged into GitHub, follow the link to your chosen GitHub repository, or use the search bar to find it on the GitHub home page.
2. Once in the repository window, click the 'Fork' drop down arrow button in the top right-hand corner.
3. Select 'Create new fork'.
4. Check the details in the window before clicking the green 'Create Fork' button.
5. You will now be able to find the copy of the repository in your own GitHub account.

## Making a Local Clone
1. Once logged into GitHub, follow the link to your chosen GitHub repository, or use the search bar to find it on the GitHub home page.
2. Once in the repository window, click the green 'Code' button.
3. To clone the repository using HTTPS, copy the link provided below the HTTPS header.
4. Open a terminal in your code editor.
5. Change the location in the current working directory to where you want the cloned directory to be created.
6. Type "git clone" into the terminal, and then paste the URL you copied and click enter.
7. This should have created a local clone of the repository.

Here is the live link to my website - <https://kateuj.github.io/coffee_cram/index.html>

# Languages

* I used HTML, CSS, Javascript and JQuery to create this site.
* Bootstrap v5.3.2 was used and built upon for creating the general layout with its grid system.

# Media Queries

* I used Media Queries to debug and override some display issues that were not rectified with Bootstrap's responsive layouts.

# Software

* I used Visual Studio Code to create, edit, preview and push my code to my Github repository.
* Git and Github for version control.
* I used Procreate for my graphics, planning and design work.
* Balsamiq for wireframes.
* Figma was used as a design board to lay out my wireframes and keep a copy of my design thought process all in one place.
* Adobe Photoshop was used to create visual mock-ups for this document, as well as reformatting all my images as .webp files to reduce file size and in turn improve the performance of my site.
* EmailJS was used in the background to help me create a functional contact form.

# Code

* **Text overlay on ingredients** - I followed this tutorial and tailored it to my own style and needs [Text image overlays](https://www.youtube.com/watch?v=Qt-70hrdJZI&ab_channel=LearnWeb)

* **Modal pop-ups** - I followed this tutorial to create my pop-ups and tailored it to my own needs [Pop-ups in Javascript](https://www.youtube.com/watch?v=r_PL0K2fGkY&ab_channel=FlorinPop)

* **Contact form** - this was based on the code used in the 'Putting it all together' emailJS exercises of Milestone 2 on Code Institute.

* **Footer** - code is based on the code used in the 'Love Running' exercise of Code Institute.

* **Thank-you page** - I used this code snippet to get the Thank You page to re-direct back to the site after 5 seconds. This was from a [Stack Overflow thread.](https://stackoverflow.com/questions/3292038/redirect-website-after-specified-amount-of-time)
![Re-direct for the thank you page code snippet](assets/readme-images/redirect-code-snippet.png)

* **Favicon** - I used a [Favicon generator](https://favicon.io/) to create the appropriate files for me to upload to my site, as well as this code snippet to install it site-wide.
![Favicon installation code snippet](assets/readme-images/favicon-code-snippet.png)

* **Timer** - I found this code snippet and edited it to suit my site's needs to make my timer function effectively. [Pause setInterval function](https://stackoverflow.com/questions/21277900/how-can-i-pause-setinterval-functions)

# Credits

* Code Institute Bootstrap lessons helped me with working out how to use the Bootstrap grid layout on my pages.
* Google fonts for ['Silkscreen' typography.](https://fonts.google.com/specimen/Silkscreen) and ['Rubik' typography.](https://fonts.google.com/specimen/Rubik)

## Content

* [Image for visual mock up at top of README document by CosmoStudio</a> on Freepik.](https://www.freepik.com/psd/desktop-tablet-phone-mockup)
* All graphics are my own work.


### Thanks

* Martina Terlevic my CI mentor, for her invaluable advice.
* [Kera Cudmore](https://github.com/kera-cudmore/readme-examples/blob/main/README.md#italic-bold-and-code) for showing how to form a README file.
* Liz Curtis my friend and fellow coder, for patiently listening, giving encouragement and brainstorming with me when I was troubleshooting.
* The big and little human beings of the Ulloa-James household who have been very patient with me, allowing me the time day or night to get my coding done.