"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
//['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
var Villagers = [];
var Players = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
];
var WereWolves = [];
var Lovers = [];
var HTargets = [];
var CultSects = [];
var Tanner;
var CultLeader;
var Hoodlum;
var Cupid;
var Roles = [
    'WereWolf',
    'WereWolf',
    'Werewolf',
    'cupid',
    'Mentalist',
    'Seer',
    'Cursed',
    'Hoodlum',
    'Tanner',
    'Bodyguard',
    'SpellCaster',
    'witch',
    'Doppleganger',
    'Cult Leader',
    'Hunter',
    'WolfCub',
];
Villagers.forEach(function (element, i) {
    if (element == 'shaun') {
        Villagers.splice(i, 1);
    }
});
function shuffleArray(array) {
    var _a;
    var newArray = __spreadArray([], array, true); // Create a copy of the original array
    for (var i = newArray.length - 1; i > 0; i--) {
        // Generate a random index from 0 to i
        var randomIndex = Math.floor(Math.random() * (i + 1));
        _a = [
            newArray[randomIndex],
            newArray[i],
        ], newArray[i] = _a[0], newArray[randomIndex] = _a[1];
    }
    return newArray;
}
var shuffledRoles = shuffleArray(Roles);
var shuffledPlayers = shuffleArray(Players);
shuffledRoles.forEach(function (element, i) {
    if (element === 'WereWolf' || 'wolfCub') {
        console.log(element);
        WereWolves.push(shuffledPlayers[i]);
    }
    else if (element === 'cupid' ||
        'Mentalist' ||
        'Seer' ||
        'Cursed' ||
        'Hoodlum' ||
        'Bodyguard' ||
        'SpellCaster' ||
        'witch' ||
        'Doppleganger' ||
        'Hunter') {
        console.log('Villagers added');
        Villagers.push(shuffledPlayers[i]);
    }
    else if (element === 'Tanner') {
        Tanner = shuffledPlayers[i];
    }
    else if (element === 'Cult Leader') {
        CultLeader = shuffledPlayers[i];
    }
    else if (element === 'Hoodlum') {
        Hoodlum = shuffledPlayers[i];
    }
    else if (element === 'Cupid') {
        Cupid = shuffledPlayers[i];
    }
});
console.log('Werewolves list');
console.log(WereWolves);
console.log('villagers list');
console.log(Villagers);
