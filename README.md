## Send Mail

Easily send mail with this API using the /mail endpoint. To use this API send a POST request to [API URL](https://easily-send-mail.herokuapp.com/mail). The request body should have the following keys
1. subject, Subject of the mail, defaults to an empty string
2. sender, Sender of the mail,
3. recipients, an array of the receivers
4. Body of the mail