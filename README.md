# What this project is
This is the portfolio website for Sai Sahu. The website serves the following purpose -

 1. Showing a detailed overview of my professional career
 2. Hosting projects made by me so that someone could quickly ensure the made projects are actually working
 3. Showcase what I am capable of doing
 4. Updating my unique Data Science courses for those who want a clear picture of the entire idea
 5. Updating my personal researches and findings 

# Why this project
**As I have been working for most of my works in self employed manner by taking contractual projects those are not disclosable, I can't show my years of experience officially by some experience letter from any reputed organization. This website, by showcasing the a few working projects, made by me, in real time gives anyone (a potential client, an assistance seeking student or a recruiter) an insight of my knowledge, experience, skills and expertise in Data Science field and create a proper impression of where I stand from current AI industry view point.**

## Website details
The website could be accessed directly by entering the IP address in the following way
[http://18.209.5.216](http://18.209.5.216) 

A proxy pass has been linked of the local IP of the hosting computer to the public IP hosting computer in the following file
`/etc/nginx/sites-enabled/aiworldlab`
Here's the content of the file
```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://172.26.13.34:5001;
        #include /etc/nginx/proxy_params;
        #proxy_redirect off;
    }
}
```