const redis = require('redis');
const promisify = require('util').promisify;

const client = redis.createClient();
const cGet = promisify(client.get).bind(client);

client.on("error", (error) => {
  console.error("Redis client not connected to the server:", error);
})

client.on("connect", () => {
  console.log("Redis client connected to the server");
})

//redis set
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, result) => {
    if (err) console.log(err.message);
    redis.print(`Reply: ${result}`);
  });
}

// redis get
const displaySchoolValue = async (schoolName) => {
  const result = await cGet(schoolName);
  console.log(result);
}

//calling the functions
(async() => {
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
})();
