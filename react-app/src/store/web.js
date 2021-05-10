const CREATE_WEB = 'web/CREATE_WEB'
const ADDTO_WEB = 'web/ADDTO_WEB'
const LOAD_WEB = 'web/LOAD_WEB'
const LOAD_WEBS = 'web/LOAD_WEBS'
const DELETE_WEB = 'web/DELETE_WEB'
const UPDATE_WEB = 'web/UPDATE_WEB'

const createWeb = (web) => ({
  type: CREATE_WEB,
  payload: web
})

const addToWeb = (web) => ({
  type: ADDTO_WEB,
  payload: web
});

const loadWeb = (web) => ({
  type: LOAD_WEB,
  payload: web
});

const loadWebs = (webs) => ({
  type: LOAD_WEBS,
  payload: webs
});

const deleteWeb = () => ({
  type: DELETE_WEB
});

const updateWeb = (web) => ({
  type: UPDATE_WEB,
  payload: web
});

// create new web
export const newWeb = (userId, web) => async (dispatch) => {
  const response = await fetch (`/api/users/${userId}/webs/create`, {
    method: 'post',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  if (response.ok){
    const web = await response.json();
    dispatch((createWeb))
  return task
  }
};

// get single web
export const showWeb = (id) => async (dispatch) => {
  const response = await fetch (`/api/users/${userId}/webs/${webId}`);

  if (response.ok) {
    const web = await response.json();
    dispatch(loadWeb(web, id));
  }
};

// get all webs
export const showWeb = () => async (dispatch) => {
  const response = await fetch (`/api/users/${userId}/webs`);

  if (response.ok) {
    const webs = await response.json();
    dispatch(loadWebs(webs));
  }
};