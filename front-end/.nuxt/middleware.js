const middleware = {}

middleware['adminApproval'] = require('..\\middleware\\adminApproval.js')
middleware['adminApproval'] = middleware['adminApproval'].default || middleware['adminApproval']

middleware['userApproval'] = require('..\\middleware\\userApproval.js')
middleware['userApproval'] = middleware['userApproval'].default || middleware['userApproval']

export default middleware
