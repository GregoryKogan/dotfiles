---@type ChadrcConfig
local M = {}

M.ui = {
	theme = "tokyonight",
	theme_toggle = {
		"tokyonight",
		"palenight",
	},
	changed_themes = {
		tokyonight = {
			base_30 = {
				black = "#24283b",
				darker_black = "#1f2336",
				statusline_bg = "#1f2336",
				black2 = "#292e41",
			},
			base_16 = {
				base00 = "#24283b",
				base01 = "#1f2336",
			},
		},
	},
	hl_override = {
		CursorLine = {
			bg = "#292e41",
		},
		ColorColumn = {
			bg = "#292e41",
		},
	},
}
M.plugins = "custom.plugins"
M.mappings = require("custom.mappings")

return M
