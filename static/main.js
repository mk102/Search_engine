Vue.component( 'detail-modal', {
    template: '#detail-modal',
    props: {
        index: Number,
        results: Object
    },
    data: function () {
        return this.results[this.index];
    }
});


var app = new Vue({
  el: '#app',
  data: {
    searchword: '',
    word: '',
    results: []
  },
  methods: {
    search: function () {
      this.word = this.searchword;
      let url = "/search?s_word=" + this.word;
      console.log(url);
      axios.get(url).then(response => {
        let results_old = this.results
        this.results = []
        for( let value of response.data) {
            this.results.push( value )
        }
        console.log(this.results);
       });
    }
  }
})