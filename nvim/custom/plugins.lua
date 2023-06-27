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
		"lazyvim.plugins.extras.formatting.prettier",
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
