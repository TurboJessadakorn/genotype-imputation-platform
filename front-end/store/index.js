export const state = () => ({
  userId: null,
  projectId: null,
  EditprojectId: null,
  fileType: "",
});

export const mutations = {
  setUserId(state, userId) {
    state.userId = userId;
  },
  //minio directory for fetch file list
  setProjectId(state, projectId) {
    state.projectId = projectId;
  },
  //current projectid for edit current project
  setEditProjectId(state, EditprojectId) {
    state.EditprojectId = EditprojectId;
  },
  setFileType(state, fileType) {
    state.fileType = fileType;
  },
};

export const actions = {
  setUserId({ commit }, userId) {
    commit('setUserId', userId);
  },
  setProjectId({ commit }, projectId) {
    commit('setProjectId', projectId);
  },
  setEditProjectId({ commit }, EditprojectId) {
    commit('setEditProjectId', EditprojectId);
  },
  setFileType({ commit }, fileType) {
    commit('setFileType', fileType);
  },
};
