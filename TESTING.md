# Instacook Testing

![Screen mock-ups of Instacook website](recipes/static/assets/readme-images/screen-mock-up.png)

[View the live project here.](https://instacook-64f0d9d64709.herokuapp.com//)

As with any project, I have been rigorously testing throughout the development process of this web application. I have documented my testing strategy that I planned before I started developing, as well as main bugs that arose whilst developing and how I approached fixing them. I have also tested my web app on different devices and asked family and friends to use and give feedback as to how to improve user experience and inform me of any bugs spotted during use.

With the scale of this project in the grand scheme of things being quite small, automated testing with softwares like Jest or Pytest, for Javascript and Python respectively. In this instance it has not been necessary, but I undestand with larger projects with more extensive functions, that this would be useful and essential. I want to use Jest and Pytest in future larger projects.

I have used a mixture of manual and automated testing while developing, both of which play a key role in forming a web application that works correctly and consistently. Automated testing can be great for doing quick overview results, for example checking code compliant with style guides etc., especially with more extensive projects and applications. Manual testing has allowed me to look at things at a deeper level, checking things like user experience design and in turn finding areas for improvement to strengthen my application as a whole. Using both has allowed me to build reliable functions and code and a higher quality end product.

# Table of Contents

1. [Automated Testing](#automated-testing)
2. [Manual Testing](#manual-testing)

# AUTOMATED TESTING

## HTML Validator - [W3C](https://validator.w3.org/)

I put every page in my site into the HTML validator. This was useful to highlight some code errors that I had missed looking through manually.

### Home Page

The validator highlighted:
* __Error:__ Missed alt tags on images.
* __Error:__"type=text/javascript" - not required.
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

#### Before
![Home page validator results before](recipes/static/assets/readme-images/home-page-validator-before.png)
#### After updates
![Home page validator results after](recipes/static/assets/readme-images/home-page-validator-after.png)

### Login Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Login page validator results](recipes/static/assets/readme-images/login-page-validator.png)

### Register Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Register page validator results](recipes/static/assets/readme-images/register-page-validator.png)

### Contact Page

The validator highlighted:
* __Error:__"type=text" on textarea - not required.
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

#### Before
![Contact page validator results before](recipes/static/assets/readme-images/contact-page-validator-before.png)
#### After updates
![Contact page validator results after](recipes/static/assets/readme-images/contact-page-validator-after.png)

### Dashboard Page

The validator would not work for the deployed link of this page, saying it was not retreiveable. This will be due to the fact that dashboard only loads when a session cookie is in place from a user login, so it would not be able to render in the validator. To work around this I added the raw code into the validator, and checked through for any justified errors. The validator, due to the fact the raw code has templating code in it that refers to the base.html for the header etc., was throwing alot of irrelevant errors, as you can see below. I checked each of them one by one, and none were justified errors that required changes.

![Dashboard page validator results](recipes/static/assets/readme-images/dashboard-page-validator.png)

### Add Cookbook Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Add cookbook page validator results before](recipes/static/assets/readme-images/add-cookbook-page-validator.png)

### Edit Cookbook Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Edit cookbook page validator results](recipes/static/assets/readme-images/edit-cookbook-page-validator.png)

### Recipes Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Recipes page validator results](recipes/static/assets/readme-images/recipes-page-validator.png)

### Search Page

The validator highlighted:
* __Error:__ Unclosed div element - closed the element and it resolved the "/li" error .
* __Error:__ Unclosed span element - removed the span element.
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

#### Before
![Search page validator results before](recipes/static/assets/readme-images/search-page-validator-before.png)
#### After updates
![Search page validator results after](recipes/static/assets/readme-images/search-page-validator-after.png)

### Add Recipe Page

The validator highlighted:
* __Error:__"type=text" on textarea - not required.
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

#### Before
![Add recipe page validator results before](recipes/static/assets/readme-images/add-recipe-page-validator-before.png)
#### After updates
![Add recipe page validator results after](recipes/static/assets/readme-images/add-recipe-page-validator-after.png)

### Edit Recipe Page

The validator highlighted:
* __Error:__"type=text" on textarea - not required.
* __Error:__ first child disabled option in dropdown, the value should be empty - emptied the values on these options.
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

#### Before
![Search page validator results before](recipes/static/assets/readme-images/edit-recipe-page-validator-before.png)
#### After updates
![Search page validator results after](recipes/static/assets/readme-images/edit-recipe-page-validator-after.png)

### Thank you Page

The validator highlighted:
* __Warning:__ Section lacks h2-h6 heading - The design structure does not require a header for this part. It is the section that holds the flash messages, but from a semantic perspective, it is better to keep the section element rather than a div so I ignored this warning.

![Search page validator results](recipes/static/assets/readme-images/thank-you-page-validator.png)

## CSS Validator - [W3C](https://jigsaw.w3.org/css-validator/)

No errors were found in my CSS code when put through the validator.
![CSS validator results](recipes/static/assets/readme-images/css-validator.png)

## JSHint Validator - [JSHint](https://jshint.com/)

### Script.js
* __Warning:__ 'let' is available in ES6 - no need to change
* __Warning:__ 'M' undefined variable - This error is a side effect of using the Materialize library. I cannot change this quote without it affecting the function with the library, so have ignored this.
* __Warning:__ 'updateQueryParams' unused variable - this is used within the search page funtionality, so this warning can be ignored in this instance.

![script.js validator results](recipes/static/assets/readme-images/scriptjs-validator.png)

### Send_mail.js
* __Warning:__ 'emailjs' undefined variable - this is the code snippet required to interact with the EmailJS API so I cannot change this.
* __Warning:__ 'sendMail' unused variable - The variable is called within the contact page in the HTML, so does not require changing.

![sendmail.js validator results](recipes/static/assets/readme-images/scriptjs-validator.png)

## Python Validator - [Code Institute Python Linter](https://pep8ci.herokuapp.com/)

### run.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code which cleared the error.

![run.py validator results](recipes/static/assets/readme-images/runpy-validator.png)

### routes.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code.
* __Error:__"expected 2 blank lines, found 1" - added extra line.
* __Error:__"line too long" - split the line up.
* __Error:__"over-indented" - reduced indentation.
* __Error:__"blank line contains whitespace" - removed white space.
* __Error:__"missing whitespace around operator" - added whitespace.

Cleared all the errors below.

![routes.py validator results](recipes/static/assets/readme-images/routespy-validator.png)

### models.py file

The validator highlighted:
* __Error:__"no new line at end of file" - added new line at the bottom of the code.
* __Error:__"expected 2 blank lines, found 1" - added extra line.
* __Error:__"line too long" - split the line up.

Cleared all the errors below.

![models.py validator results](recipes/static/assets/readme-images/modelspy-validator.png)

### __init__.py file

The validator highlighted:
* __Error:__"indentation not a multiple of 4" - fixed indent.
* __Error:__"over-indented" - reduced indent.
* __Error:__"module level import not at top of file" - this line has to be at the end of the file to be called after the rest.

![init.py validator results](recipes/static/assets/readme-images/initpy-validator.png)

## Lighthouse

To test performance and accessibility, I used Lighthouse within the Chrome Developer Tools. Accessibility was down by 1% on the search page, based on the contrast between the pink background and white recipe name text on top.

| Page | Results |
| --- | --- |
| Home Page | <img src="recipes/static/assets/readme-images/home-page-lighthouse.png" alt="Light house results for home page"> |
| Login Page | <img src="recipes/static/assets/readme-images/login-page-lighthouse.png" alt="Light house results for log in page"> |
| Register Page | <img src="recipes/static/assets/readme-images/register-page-lighthouse.png" alt="Light house results for register page"> |
| Dashboard Page | <img src="recipes/static/assets/readme-images/dashboard-page-lighthouse.png" alt="Light house results for dashboard page"> |
| Search Page | <img src="recipes/static/assets/readme-images/search-page-lighthouse.png" alt="Light house results for search page"> |
| Contact Page | <img src="recipes/static/assets/readme-images/contact-page-lighthouse.png" alt="Light house results for contact page"> |
| Add Recipe Page | <img src="recipes/static/assets/readme-images/add-recipe-page-lighthouse.png" alt="Light house results for add recipe page"> |
| Edit Recipe Page | <img src="recipes/static/assets/readme-images/edit-recipe-page-lighthouse.png" alt="Light house results for edit recipe page"> |
| Add Cookbook Page | <img src="recipes/static/assets/readme-images/add-cookbook-page-lighthouse.png" alt="Light house results for add cookbook page"> |
| Edit Cookbook Page | <img src="recipes/static/assets/readme-images/edit-cookbook-page-lighthouse.png" alt="Light house results for edit cookbook page"> |
| Recipes Page | <img src="recipes/static/assets/readme-images/recipes-page-lighthouse.png" alt="Light house results for recipes page"> |

# MANUAL TESTING

## Testing User Stories

### First time user

| Goals | How are they achieved? | Image |
| --- | --- | --- |
| As a first time user, I need to be able to understand the purpose of the site instantly and lead intuitively to thr first call-to-action. | This is achieved through a simple and clear synopsis on screen as the first thing the user sees. Right below to call-to-action to 'Register' is easily visible. | ![Home Page](/recipes/static/assets/readme-images/home-page.png) |
| I want to be able to start creating digital cookbooks quickly and add recipes to them. | Once the new user has registered they are automatically redirected to their dashboard where they can create cookbooks and the create recipes within them. | ![Dashboard Page](/recipes/static/assets/readme-images/dashboard-page.png) |
| I need to have simple instructions and layout so I am not overwhelmed by too much content or instructions. | This is achieved with clear calls to action buttons, like the buttons on each cookbook card on the user's dashboard clearly demonstrate what is possible as next steps. | ![Dashboard Page](/recipes/static/assets/readme-images/dashboard-page.png) |
| I want to be able to get inspiration and a feel for what other recipes users have uploaded. | Whether logged in or not I can filter through and view all the recipes on the site, with 3 simple dropdown filters. A link to this page is in the nav bar on all pages. | ![Search page](/recipes/static/assets/readme-images/search-page.png)|
| Should I have any questions or issues, I need to be able to contact the developer easily | The user can find a link to the contact form on all pages in both the nav bar and footer, so wherever the user is looking on the page, a link will always be clearly visible | ![Contact Page](/recipes/static/assets/readme-images/contact-page.png) |


### Returning/Frequent user
| Goals | How are they achieved? | Image |
| --- | --- | --- |
| As a returning user, I want to easily log in to my existing account to access my content. | The home page displays a prominent login call to action button and once a user is logged in, they are redirected to their dashboard to see their current cookbooks.| ![Home Page](/recipes/static/assets/readme-images/home-page.png) ![Dashboard Page](/recipes/static/assets/readme-images/dashboard-page.png)|
| I want to be able to modify or delete existing cookbooks and recipes | From their dashboard, the user can edit their cookbook names by clicking the edit button on their chosen cookbook card. They can also delete cookbooks and all recipes within that cookbook, just by clicking the delete button on the cookbook card. They will be met with a modal pop-up asking them to confirm their action, to avoid cookbooks and recipes within them being deleted accidentally. From the recipes page view, they can edit and delete recipes using the buttons at the bottom of the recipe info. | ![Dashboard Page](/recipes/static/assets/readme-images/dashboard-page.png) ![Recipes page](/recipes/static/assets/readme-images/edit-delete-recipe-buttons.png) |

## Devices Used For Testing

I have asked friends and family to test the site on their devices. This app has been tested on the following:

Poco X3 NFC - Chrome
Iphone 10 - Firefox
Ipad Pro - Safari
Huawei Matebook Pro - Microsoft Edge and Chrome
Google Pixel - Chrome

## Full Manual Testing

### Home
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login button | User is redirected to the Login page when clicked | Clicked Login button | Redirected to the login page | Pass |
| Register button | User is redirected to the Register page when clicked | Clicked the Register button | Redirected to the register page | Pass  |

### Login
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login with correct credentials | User is redirected to the their dashboard with a flash message at the top of the page that says 'Welcome "Username"' | Used correct credentials in input fields | Redirected to the Dashboard and flash message appeared | Pass |
| Login with incorrect credentials | User is kept on the Login page and a flash message appears at the top of the page saying 'Incorrect Username and/or Password' | Used incorrect credentials in input fields | Flash message appeared | Pass  |
| Register link | User is redirected to the Register page when clicked | Clicked the Register button | Redirected to the register page | Pass  |

### Register
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Register with incorrect username format | It stays on the register page and a validation message appears asking them to match the required format. | Entered a username below 5 characters, over 15 characters and with special characters. | Validation message appeared | Pass |
| Register with incorrect password format | It stays on the register page and a validation message appears asking them to match the required format. | Tried to register with a password below 5 characters, over 15 characters, only numbers, only lowercase letters, only uppercase characters, only lowercase characters and numbers, only uppercase characters and numbers, only special characters. | Validation message appeared | Pass |
| Input correct username and password. | User is redirected to their dashboard and flash message 'Registration successful'. | Registered with correct details. | Redirected to the dashboard with flash message "Registration successful".| Pass |
| Login link | Redirect to the login page. | Clicked login button | Redirected to the the login page | Pass |

### Search
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Select a meal type filter dropdown option | Should filter recipes to show only recipes that match the meal type and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a dish origin filter dropdown option | Should filter recipes to show only recipes that match the dish origin and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a star rating filter dropdown option | Should filter recipes to show only recipes that match the star rating and selection remain visible in the dropdown | Selected each of the dropdown options to view recipes filtered for each | Recipes filtered successfully and selection remained visible in dropdown | Pass |
| Select a filter dropdown option from two of the dropdowns | Should filter recipes to show only recipes that match the dish origin and selection remain visible in the dropdown | Selected a dropdown option from two dropdowns (tried all combinations) at the same time | Recipes filtered successfully  and selection remained visible in dropdown| Pass |
| Select a filter dropdown option from all three of the dropdowns | Should filter recipes to show only recipes that match the dish origin | Selected a dropdown option for all three dropdowns at the same time | Recipes filtered successfully and selection remained visible in dropdown| Pass |
| Clear selection button | Should reset all filters to blank by refreshing the page | Click the 'clear selection' button | Page refreshed successfully | Pass |
| Collapsed recipe | Should open to display recipe info when clicked | Click recipe title | Recipe info appeared correctly | Pass |

### Contact
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Input first name with over 30 characters | Should not be possible, after 30 characters, characters typed will not appear | Tried to input more than 30 characters | No characters typed over 30 characters appear | Pass |
| Leave inputs blank | Stays on page and validation message with appear prompting the user to input info into field | Left username, email and message inputs empty individually before pressing submit button | Validation message appeared to prompt user to add input | Pass |
| Email input without @ symbol | Validation message appears to prompt user to add @ sign | Input text into email input without @ symbol | Validation message is visible | Pass |
| Type a message with not enough characters | Validation message is visible | Added an input less than 10 characters long | Validation message is visible | Pass |
| Type a message with too many characters | Should not be possible, after 750 characters, characters typed will not appear | Tried to type a message with more than 750 characters | No characters typed over 750 characters appear | Pass |
| Submit will all correct format inputs | Redirect to the thank you page | Input correctly into fields and click submit button | Redirected to thank you page | Pass |

### Thank you
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Redirect countdown | Redirect to the home page after 5 second countdown | Load the thank you page | Redirected to home page successfully after 5 seconds | Pass |

### Dashboard
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add Cookbook button | Redirect to add cookbook page | Click add cookbook button | Redirected to add cookbook page successfully | Pass |
| Edit Cookbook button | Redirect to edit cookbook page for specific cookbook | Click edit cookbook button | Redirected to edit cookbook page successfully | Pass |
| View Recipes button | Redirect to recipes page with view of recipes linked to specific cookbook | Click view recipes button | Redirected to view recipes page successfully with view of recipes linked to specific cookbook | Pass |
| Add Recipe button | Redirect to add recipe page | Click add recipe button | Redirected to add recipe page successfully | Pass |
| Delete Cookbook button | Modal pop-up to confirm the user wants to delete with 'delete' and 'cancel' buttons | Click delete cookbook button | Modal pop-up appears with 'delete' or 'cancel' options. Cancel button closes the modal. Delete button successfully deletes the chosen cookbook | Pass |

### Recipes
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add Recipe button | Redirect to add recipe page | Click add recipe button | Redirected to add recipe page successfully | Pass |
| Back to cookbooks button | Redirect to dashboard page | Click back to cookbooks button | Redirected to dashboard page successfully | Pass |
| Collapsed recipe | Should open to display recipe info when clicked | Click recipe title | Recipe info appeared correctly | Pass |

### Edit Cookbook
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Pre-populated input field | Previously saved cookbook name to pre-populate the input field | Direct to the edit cookbook page from dashboard | Previously saved cookbook name was pre-populated into the input field, ready for editing | Pass |
| Save changes button | Redirect to dashboard, flash message 'Cookbook updated', with the chosen cookbook name updated on its respective card | Save changes button | Redirected to dashboard page successfully with flash message 'Cookbook updated', Cookbook name updated on card | Pass |

### Add Recipe
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Input fields left empty when form submitted | Validation message to appear "Please fill in this field" | Submit the form with each input left empty on their own | Each input had the validation message appear as expected | Pass |
| Input fields left too short when form submitted | Validation message to appear "Please lengthen this text to 5 characters or more" | Submit the form with each input short strings individually | Each input had the validation message appear as expected | Pass |
| Input fields with too many characters | Should not be possible, after max length, characters typed will not appear | Tried to type a message with more than max length in each input field | No characters typed over 750 characters appear | Pass |
| Create recipe button | Redirect to dashboard, with recipe in their chosen Cookbook card | Click create recipe button | Redirect to dashboard successfully, with recipe in their chosen Cookbook card | Pass |
| Dropdown options left empty | If a dropdown is left empty when form submitted, validation message should appear | Leave each dropdown empty individually to check | The form does not submit, but no validation message appears to tell the user why | Fail |
After adding an if statement to check if dropdowns are left blank, I re-tested.
| Dropdown options left empty | If a dropdown is left empty when form submitted, validation message should appear | Leave each dropdown empty individually to check | The form does not submit and flash message appears telling the user to make a selection | Pass |

### Edit Recipe
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Pre-populated input field | Previously saved recipe inputs to pre-populate the input field | Direct to the edit recipe page from dashboard | Previously saved recipe info was pre-populated into the input field, ready for editing | Pass |
| Save changes button | Redirect to dashboard, flash message 'Recipe updated', with the chosen cookbook name updated on its respective card | Save changes button | Redirected to dashboard page successfully with flash message 'Cookbook updated', Cookbook name updated on card | Pass |

### Add Cookbook
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Create cookbook button |  | Click create cookbook button | Redirected to dashboard page successfully with flash message 'Cookbook created' | Pass |

### 404 Page
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User tries to access an incorrect URL or page cannot cannot be found | User is redirected to the 404 page with a message displayed "Sorry this page doesn't exist", with a button linked to the Home page. | Typed an incorrect URL into address bar | Not redirected to custom 404 page. | Fail |
I revisited the 404 app route and found a code error - not '@app.errorhandler', so fixed this and tested again.
![404 App route fix](/recipes/static/assets/readme-images/404-page-route-update.png)
| User tries to access an incorrect URL or page cannot cannot be found | User is redirected to the 404 page with a message displayed "Sorry this page doesn't exist", with a button linked to the Home page. | Typed an incorrect URL into address bar | Redirected to custom 404 page | Pass |

### Log out nav bar
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User logs out using log out link in nav bar | User is redirected to login page with a message displayed "You have been logged out", and the link disappears from the nav bar, replaced by Login and Register | Click on log out link | Redirected successfully to login page with a message displayed "You have been logged out", and the link disappears from the nav bar. Register and Login reappear as links in nav bar. | Pass |


### Footer
| Feature/Action | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Links change when logged in | User logs in and links change from 'Login, Register and Contact' to 'Dashboard, Logout, Contact' | Login to registered user accunt | Links changed from 'Login, Register and Contact' to 'Dashboard, Logout, Contact' | Pass |

## Bugs

### Solved Bugs

| No. | Bug | How I solved the issue |
| --- | --- | --- |
| 1. | Pre-populated dropdown options not working in the Edit Recipe form. | Removed ‘selected’ from options.  |
| 2. | Contact form submit button triggering a new window to open Thank you page rather than just redirect. | Changed from 'window.open' to 'window.location.replace' in function.  |
| 3. | Mobile side nav not working. | Code was missing a closing bracket, so added to fix.  |
| 4. | Cookbook dropdown on add recipe and edit recipe pages showing all cookbooks on database not just particular user's cookbooks. |  |
| 5. | Recipe Ingredients and Instructions displaying as one full line without breaks on recipes page and search page. | Searched solutions and found this to add to breaks to the code [Line Breaks Solutions](https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2) |
| 6. | If dropdowns on Add and edit recipe pages not selected, no validation message appearing |  |
| 7. | Custom 404 page not appearing when incorrect URLs are created | Needed to change the app route to '@app.errorhandler(404)' [Custom 404 app route solution](https://stackoverflow.com/questions/73140435/why-custom-404-page-not-working-with-flask) |


cookbook showing all user's cookbooks not just particular user's
if dropdown not selected validation message


### Unsolved Bugs

None known at this time.