const Question = React.createClass({
  getInitialState: function() {
    return {
      numItems: null
    };
  },
  render: function() {
    let items = [];

    for (let i = 0; i < this.state.numItems; i++) {
      let num1 = Math.round(Math.random()*10+1)*1000000;
      let num2 = Math.round(Math.random()*10+1)*10000;
      let operator = ""
      let operatorValue = Math.random()*10;

      if (operatorValue < 1) {
        operator = "+";
        let answer = num1+num2;
      } else if (operatorValue < 2) {
        operator = "-";
        let answer = num1-num2;
      } else if (operatorValue < 6){
        operator = "/";
        let answer = num1/num2;
      } else {
        operator = "*";
        let answer = num1*num2;
      }

      items.push(<tr key={i}>
        <td>{num1}</td>
        <td>{operator}</td>
        <td>{num2}</td>
        <td><input></input></td>
        </tr>);
    }

    return <div>
    <input type="number"
    value={this.state.numItems}
    onChange={this.handleValueChange} />
      <table class="table table-striped b-t b-light">
        <thead>
          <tr>
            <th width="100">Number 1</th>
            <th width="100">Operator</th>
            <th width="100">Number 2</th>
            <th>Answer</th>
          </tr>
        </thead>
        <tbody>
          {items}
        </tbody>
      </table>
      </div>;
  },
  handleValueChange: function(e) {
    this.setState({
      numItems: e.target.value
    })
  }
});

ReactDOM.render(<Question />, document.getElementById('root'));
