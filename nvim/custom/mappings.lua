local M = {}

M.gopher = {
  plugin = true,
  n = {
    ["<leader>gsj"] = {
      "<cmd> GoTagAdd json <CR>",
      "(Go) Add json struct tags"
    },
    ["<leader>gsy"] = {
      "<cmd> GoTagAdd yaml <CR>",
      "(Go) Add yaml struct tags"
    },
    ["<leader>gec"] = {
      "<cmd> GoIfErr <CR>",
      "(Go) Add err check"
    }
  }
}

return M
