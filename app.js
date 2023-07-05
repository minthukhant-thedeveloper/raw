const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const app = express();
const { Buffer } = require('buffer');
const basicAuth = require('express-basic-auth');

function generateRandomString(length) {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let randomString = '';
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    randomString += characters.charAt(randomIndex);
  }
  return randomString;
}

app.use(
  basicAuth({
    users: { 'anonymous': 'mm44' },
    unauthorizedResponse: 'Unauthorized',
  })
); 

app.get('/runscript', (req, res) => {
  const scriptPath = './adduser.sh';
  const argument = req.query.name;

  exec(`sh ${scriptPath} ${argument}`, (error, stdout, stderr) => {

	const filePath = argument + ".ovpn";
	fs.readFile(filePath, 'utf8', (error, data) => {
	  if (error) {
	    console.error(`Error reading file: ${error}`);
	    res.status(500).send('Error reading file');
	    return;
	  }
	  
	  

	  const firstEncode = Buffer.from(data).toString('base64');
	  const randomString = generateRandomString(29);

	  res.send(randomString + firstEncode);



	  // // Split the file contents by line breaks
	  // const lines = data.split('\n');

	  // // Send each line as a response with line breaks
	  // lines.forEach((line) => {
	  //   res.write(line + '\n');
	  // });

	  // // Close the response
	  // res.end();
	});

  });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

