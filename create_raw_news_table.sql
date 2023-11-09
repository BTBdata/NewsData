create table raw_news_data (
ID SERIAL PRIMARY KEY,
title_id varchar(255),
title TEXT,
article_text TEXT,
source_type varchar(255),
parsed_date varchar(10)
);
