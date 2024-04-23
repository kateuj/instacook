# Instacook Testing

![Screen mock-ups of Instacook website](recipes/static/assets/readme-images/screen-mock-up.png)

[View the live project here.](https://instacook-64f0d9d64709.herokuapp.com//)

As with any project, I have been rigorously testing throughout the development process of this web application. I have documented my testing strategy that I planned before I started developing, as well as main bugs that arose whilst developing and how I approached fixing them. I have also tested my web app on different devices and asked family and friends to use and give feedback as to how to improve user experience and inform me of any bugs spotted during use.

With the scale of this project in the grand scheme of things being quite small, automated testing with softwares like Jest or Pytest, for Javascript and Python respectively. In this instance it has not been necessary, but I undestand with larger projects with more extensive functions, that this would be useful and essential. I want to use Jest and Pytest in future larger projects.

I have used a mixture of manual and automated testing while developing, both of which play a key role in forming a web application that works correctly and consistently. Automated testing can be great for doing quick overview results, for example checking code compliant with style guides etc., especially with more extensive projects and applications. Manual testing has allowed me to look at things at a deeper level, checking things like user experience design and in turn finding areas for improvement to strengthen my application as a whole. Using both has allowed me to build reliable functions and code and a higher quality end product.

## AUTOMATED TESTING

#### HTML Validator - [W3C](https://validator.w3.org/)

| Page | Errors/Warnings | Solution | Image |
| --- | --- | --- | --- |
| Welcome Page | Warning: Section lacks h2-h6 heading. | There is little use for a h2 element on this page, however a section element is still more semantically correct so ignored this warning. | <img src="./documentation/validators/html/welcome.webp" alt="HTML validator results for welcome page"> |
| Login Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/login.webp" alt="HTML validator results for login page"> |
| Register Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/register.webp" alt="HTML validator results for register page"> |
| Budget Page | N/A | N/A | <img src="./documentation/validators/html/budget.webp" alt="HTML validator results for budget page"> |
| Budgets Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page h2 header falls outside of the section element on this page. It would still be semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/budgets.webp" alt="HTML validator results for budgets page"> |
| Profile Page | N/A | N/A | <img src="./documentation/validators/html/profile.webp" alt="HTML validator results for profile page"> |
| 404 Page | N/A | N/A | <img src="./documentation/validators/html/404page.webp" alt="HTML validator results for 404 page"> |

