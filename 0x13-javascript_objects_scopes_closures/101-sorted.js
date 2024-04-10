#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [userId, occurences] of Object.entries(dict)) {
    if (!newDict[occurences]) {
        newDict[occurences] = [];
    };

    newDict[occurences].push(userId);
};

console.log(newDict);