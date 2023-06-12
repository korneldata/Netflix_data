# Netflix_data
Python (Pandas) project

In this project I used Python library (Pandas) to perform data cleaning process.

First, I imported Pandas and read .csv file:

![1](https://github.com/korneldata/Netflix_data/blob/6cb51c6e0cf1a5cd571aecd3d020ea729c6bd440/1.1.png)

Then, I took a brief look at the dataset:

![2](https://github.com/korneldata/Netflix_data/blob/626109c059cf777b63e2dfc092ea580c06f1bbfb/1.2.png)

I checked occurence of duplicated values:

![3](https://github.com/korneldata/Netflix_data/blob/626109c059cf777b63e2dfc092ea580c06f1bbfb/2.1.png)

I decided to drop 'show_id' column as unnecessary - indexes would be enough.
I also checked datatypes in my dataset:

![4](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/2.2.png)

Dates in 'date_added' column were of 'object' datatype, so I converted them to 'datetime' datatype:

![5](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/3.1.png)

I added new column: 'seasons_count' where I decided to put info about number of TV series seasons.
Then I removed info about seasons from 'duration' column by replacing with '0' values:

![6](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/3.2.png)

I also removed 'min' from 'duration' column.
Eventually, 'duration' column kept only digits:

![7](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/4.1.png)

Then I cleaned also 'seasons_count' column: 
a) removed info about movies duration,
b) removed 'Season(s)' strings, so only digits remained.
After cleaning, 'seasons_count' column looked like this:

![8](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/5.1.png)

I also renamed column 'duration' to 'duration_min':

![9](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/6.1.png)

Values in 'duration_min' column still were of 'object' datatype, so I converted them to 'int':

![10](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/7.1.png)

And I did the same with 'seasons_count' column:

![11](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/8.1.png)

Then I checked occurence of null values and changed the order of columns:

![12](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/9.1.png)

After cleaning, dataset looked like this:

![13](https://github.com/korneldata/Netflix_data/blob/999bd5853cb09735116274e302a7a6e66602eb18/10.1.png)
