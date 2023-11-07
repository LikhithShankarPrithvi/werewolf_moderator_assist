import React from 'react'

const AddingPlayers = () => {
	return (
		<div>
			<h1>Add Players</h1>
			<div className='mb-4'>
				<input
					type='text'
					id='username'
					className='shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
				/>
			</div>
		</div>
	)
}

export default AddingPlayers
