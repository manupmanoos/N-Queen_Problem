from flask import Flask,render_template,request,flash
from  algorithms import backtracking, hillclimbing, genetic_algorithm
 

app = Flask(__name__)


@app.route('/')
def home_page():
    positions = [100,100,100,100,100]
    return render_template("ChessBoard.html", size = 8,new_positions = positions, algo_temp =1)

@app.route('/algos', methods=['POST'])
def result_page():
    algo = int(request.form.get("algos"))
    board_size = int(request.form.get("board_size"))
    #if size <= 3:
        #flash(u'Solution does not exist', 'Warning')
    if algo == 1:
        positions = backtracking.main(board_size)
    elif algo == 2:
        positions = hillclimbing.main(board_size)
    else:
        positions = genetic_algorithm.main(board_size)
    new_pos =[]
    #position = positions[1]
    n= len(positions[0])
    for i,pos in enumerate(positions):
        temp_pos = []
        for j,item in enumerate(pos):
            temp_pos.append(item+j*n)
        new_pos.append(temp_pos)
    return render_template("ChessBoardLoaded.html", size = board_size ,new_positions = new_pos, algo_temp =algo)

if __name__ == "__main__":
    app.run()