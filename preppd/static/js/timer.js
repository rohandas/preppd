console.clear();

var Timer = React.createClass({
	getInitialState: function() {
    	return {
        	start: 0
        }
    },
    tick: function() {
        this.setState({
        	start: this.state.start + 1
        });
    },
    componentDidMount: function() {
    	this.interval = setInterval(this.tick, 1000);
    },
    componentWillUnmount: function() {
    	clearInterval(this.interval);
    },
    render: function() {
        return (
        	<div>
            <h4>Cumulative practice: {this.state.start}</h4>
            <h4>Average time per question: {this.state.start}</h4>
          </div>
    	)
    }
});
ReactDOM.render(<Timer />, document.getElementById('timer'))
