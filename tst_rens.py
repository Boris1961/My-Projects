from flask import Flask, render_template, request
import app

user = { 'nickname': 'Miguel' } # выдуманный пользователь
posts = [ # список выдуманных постов
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]

print(render_template("index.html", title = 'Home', user = user, posts = posts))
