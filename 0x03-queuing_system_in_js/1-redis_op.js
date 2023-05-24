const redis = require('redis');
const client = redis.createClient();

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
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, result) => {
    if (err) console.log(err.message);
    redis.print(result);
  });
}

//calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
