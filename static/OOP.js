nx.define("MyClass", {
    properties: {
        title: '',
        msg: {
            value: 'Hello World!'
        }
    },
    methods: {
        hello: function () {
            console.log(this.msg())
        }
    }
});

var foo = new MyClass();
foo.hello();

foo.msg("Hello!");
foo.hello();