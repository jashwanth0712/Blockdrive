const fs = require('fs');
const path = require('path');
const lighthouse = require('@lighthouse-web3/sdk');
key="180154a5-2728-4def-9e32-3211e7411141"
async function uploadImage(filePath, apiKey) {
  try {
    const uploadResponse = await lighthouse.upload(filePath, apiKey);
    console.log(uploadResponse);
  } catch (error) {
    console.error(error);
  }
}

const folderPath = 'Blockchain';

fs.watch(folderPath, (event, filename) => {
  if (event === 'rename') {
    const filePath = path.join(folderPath, filename);
    fs.stat(filePath, (error, stats) => {
      if (error) {
        console.error(error);
        return;
      }
      if (stats.isFile()) {
        console.log(`A new file was added: ${filename}`);
        uploadImage(filePath, key);
      }
    });
  }
});
