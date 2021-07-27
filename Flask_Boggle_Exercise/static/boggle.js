// class BoggleGame {
//     /* make a new game at this DOM id */

//     constructor(boardId, secs = 60) {
//         this.board = $("#" + boardId);


//         $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
//     }




//     async handleSubmit(evt) {
//         evt.preventDefault();
//         console.log('button submitted');
//     }
// }


class BoggleGame {
    constructor(boardId) {
        this.board = boardId;
        //from index.html form class 'add-word'
        $(".add-word").submit(function(event) {
            event.preventDefault();
            // console.log(event)
        });
        showScore() {
            $(".score", this.board).text(this.score);
        }
    }

}
}