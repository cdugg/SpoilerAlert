# Spoiler Alert

29th November 2019

## 0. Table of Contents

0. Table of Contents
1. Introduction

      1.1 Overview
      
      1.2 Business Context
      
      1.3 Glossary
      
2. General Description

      2.1 Product/System Functions
      
      2.2 User Characteristics and Objectives
      
      2.3 Operational Scenarios
      
      2.4 Constraints
      
3. Functional Requirements

      3.1 Search Database
      
      3.2 Delete Previously Selected Media
      
      3.3 Toggle Spoilers on/off
      
      3.4 Blur Spoiler Text
      
      3.5 Unblur Spoiler Text
      
4. System Architecture

      4.1 System Architecture Diagram
      
      4.2 Google Chrome Store
      
      4.3 User
      
      4.4 IMDB Database
      
      4.5 User Media Database
      
      4.6 Webpage
      
5. High-Level Design

      5.1 High-Level Design Diagram
      
      5.2 High-Level Design Description
      
6. Preliminary Schedule

      6.1 Preliminary Schedule Overview
      
      6.2 Gantt Chart
      
7. Appendices

## 1. Introduction
### 1.1 Overview
Spoiler Alert is a Chrome based web extension that blocks specific text on the internet that is deemed to be a spoiler. The user will download the extension and then select the movies and/or tv shows that they do not want spoiled. The piece of text deemed to be a spoiler will be blurred out before the page loads, ensuring that there are no chances of the user seeing it. The text can then be unblurred  by the user by clicking the blurred text. This allows for the user to have full control of what they see and don’t see. In an age where social media and streaming services are dominant, spoilers are a big concern for the average consumer and there is a clear gap in the market for this kind of application, especially for one that blocks the spoiler text before the page loads. This product will provide users with the ability to prevent popular media that they enjoy from being ruined by news articles, people that have already seen the media, and internet trolls.
### 1.2 Business Context
The product will be released as a Google Chrome web extension and therefore will make use of the extensions API provided by Google. It will then be distributed through the Chrome Developer Dashboard and published to the Chrome Web Store. Filmmakers may also have an interest in this product as there is an increasing amount of movie and tv show leaks due to various email hackings and spoiler forums. The popular movie,  Avengers: Endgame, actually ran an anti-spoiler campaign, where actors from the movie appeared in advertisements asking for people to not spoil the movie. This product could therefore be advertised by the makers of these movies and tv shows, as spoilers are an increasing concern in their field of work.
### 1.3 Glossary
**HTML:**

Acronym for **H**ypertext **M**arkup **L**anguage. This is the standard markup language for documents designed to be displayed in a web browser.

**CSS:**

Acronym for **C**ascading **S**tyle **S**heets. A style sheet language used for describing the presentation of a document written in a markup language like HTML.

**jQuery:**

JQuery is a fast, small and feature rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

**MySQL:**

MySQL is an open-source relational database management system.

**Java:**

Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible.

**PHP:**

PHP is a recursive acronym for **PHP H**ypertext **P**rocessor. It is a general-purpose programming language originally designed for web development.

**HTML Tag Attribute:**

These are modifiers for the HTML tags and they provide additional information.

## 2. General Description
### 2.1 Product / System Functions
Below is a list of the main functions of our Spoiler Alert web extension. This is a preliminary list and is open to change. Each function comes with its own parameters that will be discussed in further detail in section 3.
* Search database
* Delete previously selected movies/tv shows
* Toggle spoilers on/off for selected movies/tv shows
* Blurring spoiler text
* Unblur spoiler text

### 2.2 User Characteristics and Objectives
As Spoiler Alert will be hosted online as a Google Chrome web extension, it will be accessible to everyone with a computer and the Google Chrome browser. The target audience is avid movie goers and fans of tv shows. This audience is usually between the ages of 18 - 30, however this is not inclusive. The user interface should be simple and easy to use with a basic search bar to find the media you want blocked and then a list of the user’s already selected media. The application will of course be moderated and updated frequently to account for the release of new movies. The aim is for the product to be as minimalistic as possible and accessible for a person of any technical ability, young or old. We intend to create a user interface that can be navigated quickly and intuitively so there should be a minimal learning curve for using the product. 

### 2.3 Operational Scenarios
* **User searches for media**

The user will use the search bar at the top of the application menu to search the wide movie and tv show database. A dropdown menu will appear with suggestions as the user types. Once they find their desired media, they will select it from the dropdown menu and it will be added to their list of media to be analysed for spoilers. 
* **User cannot find desired media**

In the case of the user not being able to find their desired media, the application will alert the user that the movie/tv show that they searched for was not in the database. A “Did you mean…” alert will also appear, with a selection of media that is similar to what the user typed, in case of a misspelling by the user.
* **User visits site containing containing spoilers**

Spoiler Alert will analyse the website thought to contain spoilers preloading and will blur text thought to be a spoiler. This will mean that when the page does load, the spoilers will already be blurred so that there is no risk of the user seeing any of them. The user can then reveal the spoiler by clicking the blurred text. 

### 2.4 Constraints
The main constraints we will face regarding this project are maintenance and time.

* **Time -** Due to the constant new movie and tv show releases this application could require a lot of maintenance and updates. There is also a lot of room for this project to grow and there are many potential new features that could be added. Because of this, we will approach the March 6th deadline as a presentation of the current state of the application as it has plenty of more room to grow in the future.
* **Maintenance -** Due to the constant release of new movies and tv shows we will have to make sure our application is intuitive enough to be able to deal with the constant influx of new media. We aim for our application to be able to analyse spoilers in general to combat this, as opposed to knowing each media’s specific spoilers, it will be able to detect spoilers by analysing context and text.
* **Learning Curve -** As neither of us have ever actually developed a Chrome based web extension before, there will be a learning curve to figuring out how to implement our product as a web extension. Thankfully, Chrome has a guide on how to implement this.

## 3. Functional Requirements
### 3.1 Search Database
* **Description**

This function is the first step that the user will need to take in order to find a specific movie/tv show that they wish not to be spoiled. There will be a search bar at the top of the application and the user can search for virtually any movie/tv show in the large database.
* **Criticality**

This is clearly a very important part of or project. If a user cannot search and select their desired piece of media then the app will not be able to block the specific spoilers. The application simply does not work if the user is not able to search the database.
* **Technical issues**

The search bar itself will be made using HTML and CSS and will fit in with the overall design and layout of the application. We will handle the inputs using PHP functions to search our MySQL database. Once completed, the user will be able to search for any movie and/or TV show in our large database and select the one they wish to not to be spoiled.
* **Dependencies with other requirements**

None.
### 3.2 Delete Previously Selected Media
* **Description**

Once the user has selected the piece of media they want Spoiler Alert to target, they must also be able to then delete the media from selection if they so choose. The user may have since seen the previously specified media or simply does not care for spoilers anymore. The delete function will remove the movie/tv show from the user’s selected media list.
* **Criticality**

This function is not vital however it does allow for the user interface to be clearer and less cluttered i.e if the user has selected 20 movies/tv shows, the applications dropdown menu could be very long with the list of chosen media. Therefore, although this requirement is not vital, it is necessary for the purpose of a cleaner user interface.
* **Technical issues**

There are a variety of ways that this can be done. We will be using the jQuery method remove() to delete the specified media from the list of media selected. This will be done by implementing a trash icon beside each selected media in the list, allowing for fast and easy deletion by the user.
* **Dependencies with other requirements**

This area is dependant on the search bar requirement as the user must have selected at least one movie/tv show if they want to be able to delete it.
### 3.3 Toggle Spoilers on/off
* **Description**

This function will allow the user to toggle spoilers on and off for their selected media. This is different to the delete requirement as it still keeps the media in the users selected movie/tv shows list while also allowing for the user to turn off/on spoilers.
* **Criticality**

It is important the the user is able to very quickly change whether spoilers are blocked or not. However it is not vital to the main purpose of the application, which is to ultimately block specific spoilers. This is more of a helpful feature.
* **Technical issues**

HTML and CSS will be used to create a toggle switch. It will then use the jQuery methods on() and off() to allow for the switch between operations.
* **Dependencies with other requirements**

This area is dependant on the search bar requirement as the user must have selected at least one movie/tv show if they want to be able to switch between on/off.
### 3.4 Blur Spoiler Text
* **Description**

The application will analyse a piece of internet text and be able to classify which words and sentences contain spoilers. Spoiler Alert will then blur the text assumed to be a spoiler for the given media selected by the user.
* **Criticality**

The most critical part of the project and its main aim. The whole premise of the project is to be able to analyse and blur spoiler text so this requirement is vital.
* **Technical issues**

Potential spoilers will be analysed by using Java and MySQL to analyse text and the context of which it was written. We will then use HTML and CSS to blur the text via the blur() function.
* **Dependencies with other requirements**

Text will only be blurred for the user selected media so this will rely on the search bar to ensure the user can find specific movies/tv shows and will also rely on the delete and toggle requirements as, if a piece of media no longer needs spoilers to be blocked, the function must be aware of this.
### 3.5 Unblur Spoiler Text
* **Description**

Once the spoiler text has been blurred, the user will then be able to unblur the text by clicking on it. This will allow for the user to have total control over what they see and what they don’t.
* **Criticality**

While not vital to the project, it is very useful and important as it allows for fast and easy control by the user of what they wish to see.
* **Technical issues**

The user will be able to unblur the text by clicking the blurred text. This will be done using HTML and JavaScript, specifically the onclick HTML tag attribute.
* **Dependencies with other requirements**

Depends heavily on the blur spoiler text requirement as the text cannot be unblurred if it has not been blurred to begin with.
## 4. System Architecture
### 4.1 System Architecture Diagram 
![System Architecture Diagram](functional_spec/Drawing1.jpg "System Architecture Diagram")
### 4.2 Google Chrome Store
The application at any point can be found and downloaded by a user from the Google Chrome Web Store. Once downloaded the extension will be added to the user’s Chrome application for future use and can begin being used upon the Google Chrome application being restarted.
### 4.3 User
At any point in time a user can choose to download the extension, update their list of blocked content (this will access the IMDB Database then update the local user’s database), toggle or delete items from their list of blocked content (this will update the local user’s database), or access a web page which will run the analysis program and appropriately block spoilers.
### 4.4 IMDB Database
IMDB is an online database of information related to film and TV shows. We will be scrubbing the IMDB database for characters associated with the user’s selected media so that the application can analyse sentences and articles with these character names and be aware of spoilers involving these names. 
### 4.5 User Media Database
The user media database stores all relevant character and actor data pertaining to the selected movies on the user’s system. This will allow the spoiler detection system to appropriately identify spoilers for content specific to each individual user’s preferences.
### 4.6 Webpage
At any point in time the user can access a webpage and while doing so the spoiler identification system will be run before the page is loaded and will adjust the text on the page appropriately for the user’s selected content.
## 5. High-Level Design
### 5.1 High-Level Design Diagram
![High Level Design Diagram](functional_spec/High-Level_.png "High Level Design Diagram")
### 5.2 High-Level Design Description
* **Download Extension -** Any user is able to access the application via the Google Chrome web store where they can download and install Spoiler Alert as a web extension. It will then add a small icon to the top right of the chrome window upon restarting the application.
* **Search for Media in Extension Interface -** Upon opening the extension, a dropdown menu showing all blocked content will appear with a search bar at the top. If a user enters a valid piece of media the extension will proceed to the next step and add the given piece of media to the list below the search bar.
* **Take Character/Actor Data from IMDB -** Once a valid piece of media is searched for in the extension search bar, the character and actor data will be taken from the IMDB database for that piece of content.
* **Update Local User’s Database of Spoiler Content -** The data acquired from IMDB’s databases will then be added to the user specific content filters to appropriately keep track of what content each individual user would like to block.
* **User Actions -** Once any of the previous steps have been completed, assuming the application has been downloaded and installed, the user can proceed with browsing as normal or do a small set of actions applying to the extension itself.
  - **Add Media -** If the interface is opened by the user at any time they can search for new content and add it to their list of blocked media. This works the exact same as the previously described system and will update the user’s local database of spoiler content to block assuming the content is valid and can be located.
  - **Toggle Media -** Similarly at any point in time the user can open the extension and, underneath the search bar, all their previously added blocked media will be displayed in a list. This list will have options to toggle the content blurring on and off as well as remove the content pieces from the blocked content list. If content is toggled off the database will change a value for that specific piece of media to be looked for. If the content is deleted from the list, the user’s database will remove that piece of media from itself and appropriately be updated.
  - **Page Load -** At any point if the user loads a webpage the basic effect of the extension will be put into use. The application will scan through all available text and try to find any written content that may be considered a spoiler for any of the pieces of media in the user’s database. If a spoiler is found, the HTML file will be edited to contain proper classes assigned to the HTML tags that contain the identified spoilers. Then an additional CSS effect will be added to appropriately blur the HTML content contained in the HTML tags with the appropriate class.
  - **Click Censored Spoiler -** At any point of time, on a loaded page with spoiler content that has been identified, if a blurred set of text is clicked by the user the blurring effect will be turned off for that specific spoiler. The text will then be legible to the user and they are free to spoil anything they want for themselves. If they click the content a second time it will blur out the content again so that if they accidentally click to unblur the content they have an opportunity to get rid of it again before they read it and ruin anything for themselves.

## 6. Preliminary Schedule
### 6.1 Preliminary Schedule Overview
The Gannt chart below provides a rough schedule for our project and the order in which we will go about completing tasks. Following this schedule appropriately should allow us ample time to complete our project before the due date. The chart contains information on what tasks will be done, when they should be worked on, and how long they should take. The only anomaly is the “Demo” section which is set for a few days as we do not know what day we will be demoing our project yet.

On the chart, tasks are laid out in the order in which they will be completed. Some tasks overlap as they will need to be worked on simultaneously or may need to be revisited after their initial completion. We have allowed ourselves the most time to implement the system which will identify spoilers as that is the heart of the project. The second highest allocation of time is given to implementing the app as a Chrome Extension as neither of us have experience doing this and will have a bit of a learning curve to overcome.
### 6.2 Gantt Chart
![Gantt Chart](functional_spec/Software_Development.png "Gantt Chart")
## 7. Appendices
Gantt Chart Creation: [https://www.officetimeline.com/online/gantt-chart-maker](https://www.officetimeline.com/online/gantt-chart-maker)

“Don’t Spoil the Endgame” anti-spoiler campaign run by filmmakers: [https://www.esquire.com/uk/latest-news/a27176943/russo-brothers-dont-spoil-avengers-endgame-leak/](https://www.esquire.com/uk/latest-news/a27176943/russo-brothers-dont-spoil-avengers-endgame-leak/)

Google Chrome Web Extension Developer: [https://developer.chrome.com/extensions](https://developer.chrome.com/extensions)

IMDB Database: [[https://www.imdb.com/interfaces/](https://www.imdb.com/interfaces/)