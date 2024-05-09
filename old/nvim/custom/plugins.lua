local plugins = {
	{
		"williamboman/mason.nvim",
		opts = {
			ensure_installed = {
				-- LSP
				"gopls",
				"lua-language-server",
				"vue-language-server",
				"typescript-language-server",
				"pyright",
				"clangd",
				-- Formatters
				-- Lua
				"stylua",
				-- Go
				"gofumpt",
				"goimports",
				"goimports-reviser",
				"golines",
				-- C/C++
				"clang-format",
				"cmakelang",
				-- JS
				"prettier",
				"eslint_d",
				-- Python
				"autoflake",
				"black",
				-- Linters
				"shellcheck",
			},
		},
	},
	{
		"nvim-treesitter/nvim-treesitter",
		opts = {
			ensure_installed = {
				"go",
				"cpp",
				"python",
				"javascript",
				"typescript",
				"vue",
				"css",
				"vim",
				"lua",
				"json",
			},
		},
	},
	{
		"neovim/nvim-lspconfig",

		dependencies = {
			"jose-elias-alvarez/null-ls.nvim",
			config = function()
				require("custom.configs.null-ls")
			end,
		},

		config = function()
			require("plugins.configs.lspconfig")
			require("custom.configs.lspconfig")
		end,
	},
	{
		"zbirenbaum/copilot.lua",
		cmd = "Copilot",
		build = ":Copilot auth",
		event = "InsertEnter",
		opts = {
			panel = {
				enabled = false,
			},
			suggestion = {
				enabled = true,
				auto_trigger = true,
				keymap = {
					accept = "<C-z>",
				},
			},
		},
	},
	{
		"zbirenbaum/copilot-cmp",
		dependencies = "copilot.lua",
		opts = {},
		config = function(_, opts)
			local copilot_cmp = require("copilot_cmp")
			copilot_cmp.setup(opts)
			-- attach cmp source whenever copilot attaches
			-- fixes lazy-loading issues with the copilot cmp source
			require("lazyvim.util").on_attach(function(client)
				if client.name == "copilot" then
					copilot_cmp._on_insert_enter({})
				end
			end)
		end,
	},
	{
		"nvim-lualine/lualine.nvim",
		optional = true,
		event = "VeryLazy",
		opts = function(_, opts)
			local Util = require("lazyvim.util")
			local colors = {
				[""] = Util.fg("Special"),
				["Normal"] = Util.fg("Special"),
				["Warning"] = Util.fg("DiagnosticError"),
				["InProgress"] = Util.fg("DiagnosticWarn"),
			}
			table.insert(opts.sections.lualine_x, 2, {
				function()
					local icon = require("lazyvim.config").icons.kinds.Copilot
					local status = require("copilot.api").status.data
					return icon .. (status.message or "")
				end,
				cond = function()
					local ok, clients = pcall(vim.lsp.get_active_clients, { name = "copilot", bufnr = 0 })
					return ok and #clients > 0
				end,
				color = function()
					if not package.loaded["copilot"] then
						return
					end
					local status = require("copilot.api").status.data
					return colors[status.status] or colors[""]
				end,
			})
		end,
	},
	{
		"ray-x/go.nvim",
		dependencies = { -- optional packages
			"ray-x/guihua.lua",
			"neovim/nvim-lspconfig",
			"nvim-treesitter/nvim-treesitter",
		},
		config = function()
			require("go").setup()
			require("core.utils").load_mappings("gopher")
		end,
		event = { "CmdlineEnter" },
		ft = { "go", "gomod" },
		build = ':lua require("go.install").update_all_sync()', -- if you need to install/update all binaries
	},
	{
		"iamcco/markdown-preview.nvim",
		config = function()
			vim.fn["mkdp#util#install"]()
			vim.g.mkdp_filetypes = { "markdown", "md" }
		end,
		ft = { "markdown", "md" },
	},
}

return plugins
