// Import the 'readline' module
import { Console, count } from 'console'
import * as readline from 'readline'

//['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

interface Player {
	name: String
	role: String
}

const Villagers: Array<string> = []
const Players: Array<string> = [
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
]
const WereWolves: Array<string> = []
const Lovers: Array<string> = []
const HTargets: Array<string> = []
const CultSects: Array<string> = []
var Tanner: String
var CultLeader: String
var Hoodlum: String
var Cupid: String

const Roles: Array<string> = [
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
]

Villagers.forEach((element, i) => {
	if (element == 'shaun') {
		Villagers.splice(i, 1)
	}
})

function shuffleArray<T>(array: T[]): T[] {
	const newArray = [...array] // Create a copy of the original array

	for (let i = newArray.length - 1; i > 0; i--) {
		// Generate a random index from 0 to i
		const randomIndex = Math.floor(Math.random() * (i + 1))

		// Swap elements at randomIndex and i
		;[newArray[i], newArray[randomIndex]] = [
			newArray[randomIndex],
			newArray[i],
		]
	}
	return newArray
}

const shuffledRoles = shuffleArray(Roles)
const shuffledPlayers = shuffleArray(Players)

shuffledRoles.forEach((element, i) => {})

shuffledRoles.forEach((element, i) => {
	if (element === 'WereWolf' || 'wolfCub') {
		console.log(element)
		WereWolves.push(shuffledPlayers[i])
	} else if (
		element === 'cupid' ||
		'Mentalist' ||
		'Seer' ||
		'Cursed' ||
		'Hoodlum' ||
		'Bodyguard' ||
		'SpellCaster' ||
		'witch' ||
		'Doppleganger' ||
		'Hunter'
	) {
		console.log('Villagers added')
		Villagers.push(shuffledPlayers[i])
	} else if (element === 'Tanner') {
		Tanner = shuffledPlayers[i]
	} else if (element === 'Cult Leader') {
		CultLeader = shuffledPlayers[i]
	} else if (element === 'Hoodlum') {
		Hoodlum = shuffledPlayers[i]
	} else if (element === 'Cupid') {
		Cupid = shuffledPlayers[i]
	}
})

console.log('Werewolves list')
console.log(WereWolves)

console.log('villagers list')
console.log(Villagers)
