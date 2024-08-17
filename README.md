# Company Search Application

## Overview

This project is a web application that allows users to search for company information. It integrates MongoDB and Elasticsearch to provide efficient search and suggestion capabilities. Users can type in the search box to get suggestions and view detailed information about companies.

## Features

- **Search Suggestions**: Provides real-time search suggestions as users type in the search box.
- **Search Results**: Displays a list of matching companies based on the search query.
- **Company Details**: Shows detailed information about a specific company when selected from the search results.

## Prerequisites

- **Python**: Ensure Python 3.12.1 or later is installed.
- **Django**: The web framework used for the application.
- **Elasticsearch**: For full-text search capabilities.
- **MongoDB**: To store the company data.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/sachnaror/company-search.git
    cd company-search
    ```

2. **Install Dependencies**

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Install Elasticsearch and MongoDB:

    Follow the official installation guides:
    - [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
    - [MongoDB](https://www.mongodb.com/docs/manual/installation/)

3. **Set Up the Database**

    - Import the company data into MongoDB:

      ```bash
      mongoimport --db companyDB --collection companies --file /path/to/CompanyExtracted.json --jsonArray
      ```

4. **Run Elasticsearch**

    Ensure Elasticsearch is running on `http://localhost:9200`.

5. **Run Migrations**

    Apply Django migrations:

    ```bash
    python manage.py migrate
    ```

6. **Start the Django Development Server**

    ```bash
    python manage.py runserver
    ```

    Visit `http://localhost:8000` in your web browser.

## Code Overview

- **`views.py`**: Contains the view functions for handling search and suggestions.
- **`index.html`**: The main page where users can input search queries and view search results.
- **`search_results.html`**: Displays the results of the search query.
- **`company_detail.html`**: Shows detailed information about a specific company.

## View Functions

- **`index(request)`**: Renders the main search page.
- **`search(request)`**: Handles search requests and displays results.
- **`company_detail(request, registration_number)`**: Displays detailed information for a specific company.
- **`search_suggestions(request)`**: Provides real-time search suggestions based on user input.

## Elasticsearch Integration

- **Index Name**: `company_index`
- **Mapping**: Ensure the index mapping is set up to match the fields from MongoDB.

## Troubleshooting

- **404 Errors**: Ensure that the URL patterns in `urls.py` are correctly configured and that the `search_suggestions` view is properly implemented.
-
- **JSON Parsing Errors**: Verify that the JSON data in the `CompanyExtracted.json` file is correctly formatted and matches the expected schema.


## Contact

For any questions or issues, please contact [Sachin](mailto:schnaror@gmail.com).
