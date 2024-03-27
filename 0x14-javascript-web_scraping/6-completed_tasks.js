#!/usr/bin/node

const request = require('request');

if (process.argv[2] !== undefined) {
  const url = process.argv[2];

  request(url, (err, res, body) => {
    if (err) { console.error(err); } else {
      const tasks = JSON.parse(body);
      const completedUserAndTasks = {};
      const completedTasks = tasks.filter(task => task.completed === true);
      completedTasks.forEach(task => {
        if (completedUserAndTasks[task.userId] === undefined) { completedUserAndTasks[task.userId] = 1; } else { completedUserAndTasks[task.userId]++; }
      });
      console.log(completedUserAndTasks);
    }
  });
}
