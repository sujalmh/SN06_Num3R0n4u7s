from flask import Flask, render_template, request, redirect, url_for
from score_posts import results
from score_post_comments import result_post_comments
from generate_posts_bard import generate_posts_out

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile_analysis')
def profile_analysis():
    return render_template('profile_analysis.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('lead.html')

@app.route('/post_analysis')
def post_analysis():
    return render_template('post_analysis.html')

@app.route('/generate_posts')
def generate_posts():
    return render_template('generate_posts.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        linkedin_url = request.form.get('linkedin_url', '')
        posts, post_score_positive, post_score_emotion, final_sorted_emotions, final_score_positive, name, img_url = results(linkedin_url, 200)

        return render_template('result.html',
                               final_score_positive=final_score_positive,
                               final_sorted_emotions=final_sorted_emotions,
                               img_url=img_url,
                               name=name,
                               posts_data=zip(posts, post_score_positive, post_score_emotion))

@app.route('/result_post', methods=['POST'])
def result_post():
    if request.method == 'POST':
        linkedin_post_url = request.form.get('linkedin_post_url', '')
        post, summ_pos, summ_neu, summ_neg, per_pos = result_post_comments(linkedin_post_url)

        return render_template('result_post.html', post=post,                           
                               summ_pos=summ_pos,
                               summ_neu=summ_neu,
                               summ_neg=summ_neg,
                               per_pos=per_pos)

@app.route('/result_gen_post', methods=['POST'])
def result_gen_post():
    if request.method == 'POST':
        outputs = generate_posts_out()

        return render_template('result_gen_post.html',
                               outputs=outputs)



if __name__ == '__main__':
    app.run(debug=True)
