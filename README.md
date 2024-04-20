# Scrape This Site - Sandbox

A collection of projects that we'll use to learn web scraping.

- **Countries of the World: A Simple Example**

  A single page that lists information about all the countries in the world.

  There are following information that can be scraped...
  
    - Country Name
    - Country Capital
    - Country Population
    - Country Area

- **Hockey Teams: Forms, Searching and Pagination**

  Browse through a database of NHL team stats since 1990 and build a scraper that handles common website interface components.

  There are following information that can be scraped...

    - Team Name
    - Year
    - Wins
    - Losses
    - OT-Losses
    - Win %
    - Goals For (GF)
    - Goals Against (GA)
    - Difference (+ / -)

- **Oscar Winning Films: AJAX and Javascript**

  Click through a bunch of great films. Learn how content is added to the page asynchronously with Javascript and how you can scrape it.

  There are following information that can be scraped...

    - Title
    - Nominations
    - Awards
    - Best Picture
  
- **Turtles All the Way Down: Frames & iFrames**

  Some older sites might still use frames to break up thier pages. Modern ones might be using iFrames to expose data. Learn about turtles as you scrape content inside frames.

  There are following information that can be scraped...

  - Species Name
  - Discription

# How to Run?

1. Clone this repository.
   
   ```
   git clone https://github.com/VIIVIIIIX/scrape-this-site-sandbox.git
   ```

2. Create a virtual environment.
   
   ```
   cd scrape-this-site-sandbox
   python3 -m venv .venv
   ```

3. Activate the virtual environment and install necessary libraries.
   
   ```
   cd .venv
   source ./bin/activate
   cd ..
   pip install -r requirements.txt
   ```
   
4. Change the directory and run the code to generate the csv containing data.

  - Countries Of the World

    ```
    cd countries-of-the-world
    python3 countries.py
    ```
     
  - Hockey Teams

    ```
    cd hockey-teams
    python3 hockey-teams.py
    ```

  - Oscar Winning Films

    ```
    cd oscar-winning-films
    python3 oscar.py
    ```
    
  - Turtles iframes

    ```
    cd turtles-iframes
    python3 turtles.py
    ```
