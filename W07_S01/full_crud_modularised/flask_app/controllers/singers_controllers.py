from flask_app import app
from flask import request , redirect, render_template
from flask_app.models.singer_model import Singer

# Show All Singers
@app.route('/')
def index():
    singers_list = Singer.get_all()
    return render_template("index.html", singers_list = singers_list)

# Show One Singer
@app.route("/singers/<int:singer_id>")
def one_singer(singer_id):
    data = {'id':singer_id}
    one_singer = Singer.get_one(data)
    return render_template("one_singer.html", singer = one_singer)

# New Singer
@app.route("/singers/new")
def new_singer():
    return render_template("new_singer.html")


# Create New Singer
@app.route("/singers/create", methods=["post"])
def create_singer():
    print(request.form,"*"*10)
    # Request.form ===  ImmutableMultiDict([('name', 'Rex'), ('nationality', 'Germanysjvbksjvbsjkdv'), ('image', 'aaaaaaaaaaaaaaaaaaaaaaaaa'), ('rate', '20'), ('best_song', 'szdfgh')]) **********
    Singer.create(request.form)
    return redirect('/')

# Edit one Singer
@app.route("/singers/<int:singer_id>/edit")
def edit_singer(singer_id):
    singer_to_edit = Singer.get_one({'id':singer_id})
    return render_template("edit_singer.html", singer = singer_to_edit)
# Update Singer
@app.route("/singers/<int:singer_id>/update", methods=['post'])
def update_singer(singer_id):
    data = {
        **request.form,'id':singer_id
    }
    Singer.update(data)
    return redirect(f'/singers/{singer_id}')
    
# Delete Singer
@app.route("/singers/<int:singer_id>/delete")
def delete_singer(singer_id):
    Singer.delete({'id':singer_id})
    return redirect("/")