import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  const user = createUser();
  const promises = [photo, user];
  Promise.all(promises)
    .then((result) => {
      console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
