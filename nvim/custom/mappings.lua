local M = {}

M.gopher = {
	plugin = true,
	n = {
		["<leader>gec"] = {
			"<cmd> GoIfErr <CR>",
			"(Go) Add err check",
		},
	},
}

return M
