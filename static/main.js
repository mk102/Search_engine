Vue.component( 'detail-modal', {
    template: '#detail-modal',
    props: {
        index: Number,
        results: Object
    },
    data: function () {
        return this.results[this.index];
    }
} );

var app = new Vue({
  el: '#app',
  data: {
    s_g_word: '',
    s_n_word: '',
    n_word: '',
    g_word: '',
    results: [],
    showContent: false
  },
  methods: {
    search: function () {
      this.g_word = this.s_g_word;
      this.n_word = this.s_n_word;
      let url = "/search?s_g_word=" + this.g_word + "&s_n_word=" + this.n_word;
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