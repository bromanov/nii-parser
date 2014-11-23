/** @jsx React.DOM */

var EmailForm = React.createClass({
  getInitialState: function() {
    return {email: ""};
  },

  handleClick: function(event){
    $.ajax({
      url: ("/api/signup/" + this.state.email),
      method: "GET"
    });
    this.setState({email: ""})
  },

  handleUpdate: function(event){
    this.setState({email: event.target.value});
    return true
  },

  render: function() {
    var Glyphicon = ReactBootstrap.Glyphicon;
    var Input = ReactBootstrap.Input;
    var Button = ReactBootstrap.Button;
    return (
            <div>
              <Input onChange={this.handleUpdate} name="query" type="text" placeholder="Оставьте свою почту" value={this.state.email} width="400"></Input>
              <Button id="savebutton" onClick={this.handleClick}>Sign Up</Button>
            </div>
    );
  }
});

React.renderComponent(
  <EmailForm></EmailForm>,
  document.getElementById('app')
);