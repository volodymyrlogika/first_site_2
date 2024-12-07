from flask import Flask, render_template

from db_scripts import DatabaseManager

app = Flask(__name__)  # Створюємо веб–додаток Flask
db = DatabaseManager("blog.db")

@app.context_processor
def get_categories():
    categories = db.get_all_categories()
    return dict(categories=categories)

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    articles = db.get_all_articles()
    return render_template("index.html", articles=articles)  # html-сторінка, що повертається у браузер


@app.route("/articles/<int:article_id>")  # Вказуємо url-адресу для виклику функції
def article_page(article_id):
    article = db.get_article(article_id)
    return render_template("article_page.html", article=article)  # html-сторінка, що повертається у браузер


@app.route("/categories/<int:category_id>")  # Вказуємо url-адресу для виклику функції
def category_page(category_id):
    articles = db.get_category_articles(category_id)
    return render_template("index.html", articles=articles)  # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження