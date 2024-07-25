import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const obj = { fileName, firstName, lastName };
  return Promise.allSettled([uploadPhoto(obj), signUpUser(obj)]);
}
